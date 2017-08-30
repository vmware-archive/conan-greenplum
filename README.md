# Greenplum Conan Dependencies

This repository contains conan package files (http://conan.io) for Greenplum  dependencies.  Although it's designed to be primarily a C/C++ package manager it does have functionality that will allow us to build packages in other languages as well

## Repository Structure

Each dependency should be tracked by recipes in their own directory and each version should have it's own recipe file.  As a dependency is rev'd to a new version, a new recipe file should be added.

## Installing Conan

```
        pip install conan
```

## Hosting Packages

We are hosting the packages in a [Bintray](http:bintray.com) repository.  If you want to simply consume packages then you only need to update your list of remotes via the command:

```
	conan remport add <REMOTE_NAME> https://api.bintray.com/conan/greenplum-db/gpdb-oss 
```

If you wish to contribute packages or update, please create a user on Bintray and request membership to the **greenplum-db** organization

## Creating Packages

### Registration (If not registered with bintray)

  1. Register at https://bintray.com/signup, use `Signup with Github`.
     * Authorize bintray
     * Set Organization Id to your preferred name
     * Chose Country
     * Complete Registration
  2. Once logged in, go to https://bintray.com/greenplum-db and Click `Join`.
  3. Once logged in, go to `Edit Profile` -> `API Key` -> `Show`. This will be your password to upload packages to bintray.

### Build and Publish packages
  1. Clone conan repostiory into your local workspace 
     * `git clone git@github.com:greenplum-db/conan.git`
  2. Go to the conan repository directory in your local workspace
     * `cd conan`
  3. Add conan remote repository
     * `conan remote add <REMOTE_NAME> https://api.bintray.com/conan/greenplum-db/gpdb-oss`
  4. Build `ORCA` or `XERCES-C` (For now xerces-c is stable and no changes are being pushed in, so you may not need to build xerces-c). If building gpxerces, replace orca/<orca_version> with xerces-c/<xerces_version> in the commands below.
     * Update orca_version in orca_build_environ_vars.sh.
     * `source orca_build_environ_vars.sh`
       * It will export orca_version and gpxerces_version environment variables used by conan
     * `cd orca`
     * `conan export gpdb/stable`
       * It will cache the local conanfile.py present in the current directory
     * `conan install orca/v2.40.2@gpdb/stable --build=missing`
       * It will build orca v2.40.2 package
       * Replace v2.40.2 with the version you want to build
       * By default, build_type is Release. To set build_type to debug, you can execute `conan install -s build_type=Debug  orca/v2.40.2@gpdb/stable --build`
     * `conan user -p "<API KEY>" --remote <REMOTE_NAME> <GITHUB_USER_NAME>`
       * It will set the credentials used to publish the packages to bintray. 
       * Ex: conan user -p "c5aaasdfasdfasdfasdfadsfasc6386afe7028f0579c1" --remote conan-gpdb bhuvnesh2703
     * `conan upload orca/v2.40.2@gpdb/stable --all -r=<REMOTE_NAME>`
       * It will upload the v2.40.2 orca package to bintray

A tutorial and further instructions on how to write packages can be found at the [Conan site](http://conanio.readthedocs.io/en/latest/).  Further help can be found either on the [Conan github](https://github.com/conan-io/conan) or on the [Greenplum Mailinglist](gpdb-dev@greenplum.org)
