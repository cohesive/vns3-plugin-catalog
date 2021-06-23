# VNS3 Plugin Catalog
This is the master list of plugins that are installable in VNS3. They include Cohesive Networks created plugins as well as third party maintained plugins.

## Building a plugin
VNS3 plugins are docker containers running inside a VNS3 controller. All plugins in the catalog should be compatible with the [Plugin Manager](https://docs.cohesive.net/docs/network-edge-plugins/plugin-manager). You can learn more about building custom plugins here.

## Adding a plugin to the catalog
1. Contact Cohesive Networks for repository write access. Send an email to support@cohesive.net with a Subject "VNS3 Plugin Catalog Access Request"
2. After recieving access, clone the repository, create a branch called `add-plugin-[your-plugin-name]`
3. Create new directory under the plugins directory. The name must be unique amongst all plugins and should be lowercase containing letters, numbers or dashes.
4. In the directory created in #3, create a new file called plugin.yaml
5. Populate your plugin.yaml file with the following:


**Name and Description** - required - This will be displayed in the plugin catalog (required)
```
name: Plugin Name
description: Collect, monitor and alert on packetloss statistics.
```

**Documentation and Support** - required - A link to documentation for your plugin should also be provided and will be linked to in the VNS3 catalog
```
documentation: https://docs.cohesive.net/docs/network-edge-plugins/overlay-engine/
support: https://support.cohesive.net
```

**Image url or Setup Url** - required - One of image_url or setup_url should be provided. Ideally an image url can be provided such that VNS3 can immediately install your plugin. If instead you require a workflow whereby a client must first sign up with your service before being able to download a VNS3 plugin, the setup_url should be used linking to how to acquire this plugin for download.
```
image_url: https://vns3-containers-read-all.s3.amazonaws.com/Overlayengine/overlayengine_20200510.tar.gz
setup_url: https://how.to.setup.com
```

**Categories** - required - a list of categories in which your plugin falls
```
categories:
  - performance
```

The available categories are:
- performance
- monitoring
- logging
- security
- proxy
- networking

If your plugin does not fall into one of the provided categories and would like to suggest a new category, feel free to put a pull request into this repo editing this README.md. Please create a branch called `add-category-[new category]` for your pull request. Please link to the new plugin pull request requiring the new category.

**Provider code** - required - This code will be provided by Cohesive Networks during step 1 of the above process
```
provider_code: 222222
```

**Tags** - key-value attributes for associating arbitrary data with your plugin
```
tags:
  baseOS: Ubuntu 20.04
  ui: true
```

**Keyphrases** - a list of keyword phrases (such as synonyms) to be used for search purposes 
```
keyphrases:
  - Web application firewall
  - intrusion detection
```

**Logo** - an image to display in VNS3 console. You may commit a small logo to the directory and refer to it directly in your plugin.yaml. For example, you can place an image at `[my-plugin-dir]/images/my-plugin-logo.png`. It should be [optimized](https://tinypng.com/) and sized as 45px by 45px.
```
logo: images/my-plugin-logo.png
```


## Installing
All plugins in master will be displayed in VNS3 on the install plugins page.

![Install page picture](https://cohesive-networks.s3.amazonaws.com/plugins/plugin-catalog.png "VNS3 plugin install page")
