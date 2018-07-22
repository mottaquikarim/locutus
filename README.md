# Locutus (of Borg)

![img](https://media3.giphy.com/media/zDtyh2ISgzZIY/giphy.gif)

☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️☠️

*Serverless functions that enable various home automation tasks via voice, text, CRON and external service integration.*

A series of AWS Lambda functions, managed by Serverless Framework, that handle various home automation tasks via integrations.


## TODOS:

* CI integration with Travis!
* Set up functional testins with Makefile, write functional and unit tests
* Set Up Twilio support for the ecovacs service

## Table of Contents
* **[System Requirements](#system-requirements)**
* **[Usage and Installation](#usage-and-installation)**
* **[Secrets](#secrets)**
* **[Deployment](#deployment)**
* **[Todos](#todos)**
* **[Clients](#clients)**
* **[Useful Links](#useful-links)**

### System Requirements

Here are the main tools and runtimes that I used to develop this project locally

```
$ docker -v # Docker version 17.12.0-ce (or greater)

$ docker-compose -v # docker-compose version 1.18.0

$ node -v # v8.1.2, or latest

$ python3 --version # Python 3.6.5, or Py3+
```

### Usage and Installation

From terminal, pull down this repo:

```
$ git clone https://github.com/mottaquikarim/locutus
```

Then, assuming docker is running:

```
$ make test
```

Will build app and run (essentially nonexistent) tests.

### Secrets

Secrets are managed through environment variables, fed in via CI (Travis) or manually exported in local environment. To run deployment and/or ftest in local environment, first export all env variables as defined in `envvars.sample`. **NOTE**: the app's Dockerfiles copy `envvars.sample` to `envvars`, which is used for container builds. 


### Deployment

Serverless Framework is used to handle deployment. Look at [Serverless](https://serverless.com/framework/docs/getting-started/) getting started guide. 

Assuming `~/.aws/credentials` are exported to your envirnonment, simply run:

```
$ make clean deploy stage=dev
```

Note that `stage` is a concept from AWS Lambda, it can be any arbitrary value (which will be reflected in the deployed lambda url, it is used mainly to segment environments).

If you don't have `~/.aws/credentials` folder or are not sure why it is needed, please take a look at [these docs](https://serverless.com/framework/docs/providers/aws/cli-reference/).

### Useful Links

[Serverless Framework Alexa Skills conf](https://serverless.com/framework/docs/providers/aws/events/alexa-skill/)

The way to allocate the skills ref to a lambda function has changed and may potentially change again in the future.

[sucks](https://github.com/mottaquikarim/sucks) 

Sucks is a great wrapper for XMPP protocol for communicating with the [EcoVac DeeBot N79S](https://www.amazon.com/gp/product/B077HW9XM7/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1). Had to fork to pull in a change that has not yet been merged to master but is necessary to properly authenticate with the bot.

[Debugging N79S WiFi connectivity issues](http://xiaoleicestustc.blogspot.com/2015/12/why-i-cannot-add-my-ecovacs-robot-to.html)

Had some trouble getting the vac to initialyl connect to wifi network.

[Alexa Smart Home Skill Example)(https://github.com/alexa/alexa-smarthome/blob/master/sample_lambda/python/lambda.py)

This starter was super helpful towards understanding how to set up the Alexa Smart Home skill. This [tutorial](https://github.com/alexa/alexa-smarthome/wiki/Build-a-Working-Smart-Home-Skill-in-15-Minutes) was a bit much (and a little outdated) but enough to get started.

Also, official [AWS docs](https://developer.amazon.com/docs/smarthome/steps-to-build-a-smart-home-skill.html#configure-the-smart-home-service-endpoint) for this.
