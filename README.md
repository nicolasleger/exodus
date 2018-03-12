# Exodus
**Exodus** is meant to:
  * download a bunch of APK files from *Google Play*
  * find trackers signature in unzipped APK
  * retrieve application information like version, handle, ...
  * manage Android VirtualBox VM
  * install and run Android applications
  * analyze the network traffic generated by the application
  * retrieve DNS queries and responses
  * retrieve HTTP posted data
  * generate JSON report

# Development environment

Install [vagrant](https://www.vagrantup.com/) and execute:

```
vagrant up
```

Now, you can [make a tea](https://wiki.laquadrature.net/TeaHouse).

Or you can follow the [step by step installation](doc/install.md) guide.

# Analyse an application

Browse [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and enter your login and password. Then,
browse [http://127.0.0.1:8000/analysis/submit/](http://127.0.0.1:8000/analysis/submit/), specify an application handle
and click on submit.
