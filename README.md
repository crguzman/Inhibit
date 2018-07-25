google-compute-engine-selenium
============

1.	Go to [your cloud console compute engine](https://console.cloud.google.com/compute/instances)
2.	create a new instance of VM, you can simply use default settings. this should be a Debian image
3.	ssh into your instance after it's been setup
4.	issue the following commands:

```
wget https://raw.githubusercontent.com/crguzman/Inhibit/master/install.sh && chmod +x install.sh && ./install.sh &&  ./start_headless.sh && ./Inhibit.py
```

...after about 5 minutes, you should see

```
browsing with chrome, http://www.python.org
Welcome to Python.org
```
To continue using it just re run your engine and:
chmod +x install.sh &&  ./Inhibit.py

that means you've succeeded.
