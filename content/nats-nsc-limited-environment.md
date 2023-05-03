Title: NATS - restricted account creation for authentication
Date: 2023-05-03 21:00
Category: Programming, NATS

# Bringing DMZ concept into NATS
This article will show you how to prepare a working environment, where it is possible to issue user credentials only for a specific account. It is useful for scenarios where we want to create a login service which will distribute our credentials, but for security reasons we don't want to give it to much permissions. 

# Basic setup

1. Install nsc - [NSC github page](https://github.com/nats-io/nsc#install)
2. Generate operator, account and user using `nsc init`


# NATS configuration
A NATS Based resolver must be active in order for this to work. Basic configuration can be obtained using nsc:
```bash
 nsc generate config --nats-resolver
```
Appending output of this command to nats-server config file will enable a JWT resolver. However it will initially only contain information about service account. In order to push other accounts, you'll need to execute two more commands.
```bash
# This will edit your local nsc operator config to include resolver URL 
nsc edit operator --account-jwt-server-url nats://localhost # replace localhost with your server address
# This will push your accounts (other than service account)
nsc push -A
```

# Creating DMZ
Now, let's create a special, restricted account. All users in this account will be created by a service.
```bash
nsc add account -n dmz
```
When we'll be crating this service, we'll want to give it as little permissions as possible. Basically it should be able only to create new users in DMZ account. Unfortunately I was unable to come up with streamlined cli steps, but we can just move some files around. Our environment should contain only:

1. Account nkey for signing new users
2. Account jwt file
3. Operator jwt file

If we've made fresh operator with `nsc init` and added account with `nsc add account dmz`, our nsc data folder (~/.local/share/nats/nsc) should look like this:
```bash 
~/.local/share/nats/nsc
├── keys
│   ├── creds # User credentials - we don't need those
│   │   └── init_oau
│   │       ├── SYS
│   │       │   └── sys.creds
│   │       └── init_oau
│   │           └── init_oau.creds
│   └── keys
│       ├── A # We'll need one of those keys, the one for our dmz account
│       │   ├── AA
│       │   │   └── AAAJB42VABX4ZBOGNZXOJAYYOLZZQTUDKFX7MFXJJKLJEF4ZUH7WYYLB.nk
│       │   ├── C3
│       │   │   └── AC3NVTPPKHLYFIYJPWG22EDBGSP6NUUZX5CIAENC66SB56VZDJPOSYL6.nk
│       │   ├── CM
│       │   │   └── ACM5EWFMQGI5PUTE6DVGCWCSLHHBLQEGS3KHOIEDHMSRTK3RNC3ERYG2.nk
│       │   └── DP
│       │       └── ADPEGYOE5FBEZJMSHOFROHSICT56BM67Q6MGAI7VCQW5NCZHOUPDTBJW.nk
│       ├── O
│       │   └── B4
│       │       └── OB4E3HUYT7ZPFBQU7CV27G6HYURJGFWTVAQRJODI4OHC4N5KO7MI56G2.nk
│       └── U
│           ├── B5
│           │   └── UB5SJKNRWQLVXOH45RARZLIV2DUKAUFVGAUIQSADQGAIWP6IETZJTRRL.nk
│           └── D5
│               └── UD5UM4T2NON62N4QA4N4EK2GJDTOOPAI26MHCZOKSJ4C3JQRUJMY72QJ.nk
└── stores
    └── init_oau
        ├── accounts
        │   ├── SYS
        │   │   ├── SYS.jwt
        │   │   └── users
        │   │       └── sys.jwt
        │   ├── dmz
        │   │   └── dmz.jwt # account JWT - we need this
        │   └── init_oau
        │       ├── init_oau.jwt
        │       └── users
        │           └── init_oau.jwt
        └── init_oau.jwt # operator JWT - we need this
```
To find out which one of account keys we need, run `nsc describe account dmz`. Account ID is a public key of our dmz account and a filename of our key. After cleanup, the same folder should look like this:
```bash 
~/.local/share/nats/nsc
├── keys
│   └── keys
│       └── A
│           └── C3 # account private key
│               └── AC3NVTPPKHLYFIYJPWG22EDBGSP6NUUZX5CIAENC66SB56VZDJPOSYL6.nk
└── stores
    └── init_oau
        ├── accounts
        │   └── dmz
        │       └── dmz.jwt # account JWT - we need this
        └── init_oau.jwt # operator JWT - we need this
```
Now we have a minimal nsc setup for DMZ user creation!

# Summary
This approach allows you to limit risks when creating NATS authentication services. Now the only thing to do is to create your microservice.

# Links
[NATS docs](https://docs.nats.io/)
