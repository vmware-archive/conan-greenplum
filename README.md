# Greenplum Conan Dependencies

This repository contains conan package files (http://conan.io) for Greenplum  dependencies.  Although it's designed to be primarily a C/C++ package manager it does have functionality that will allow us to build packages in other languages as well

## Repository Structure

Each dependency should be tracked by recipes in their own directory and each version should have it's own recipe file.  As a dependency is rev'd to a new version, a new recipe file should be added.

## Hosting Packages

We are hosting the packages in a [Bintray](http:bintray.com) repository.  If you want to simply consume packages then you only need to update your list of remotes via the command:

```
	conan remport add <REMOTE_NAME> https://api.bintray.com/conan/greenplum-db/gpdb-oss 
```

If you wish to contribute packages or update, please create a user on Bintray and request membership to the **greenplum-db** organization

## Creating Packages

A tutorial and further instructions on how to write packages can be found at the [Conan site](http://conanio.readthedocs.io/en/latest/).  Further help can be found either on the [Conan github](https://github.com/conan-io/conan) or on the [Greenplum Mailinglist](gpdb-dev@greenplum.org)