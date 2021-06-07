# VNS3 Plugin Catalog
This is the master list of plugins that are installable in VNS3. They include Cohesive Networks created plugins as well as third party maintained plugins.

## Adding a plugin
1. Contact Cohesive Networks for repository write access. Send an email to support@cohesive.net with a Subject "VNS3 Plugin Catalog Access Request"
2. After recieving access, clone the repository, create a branch called `add-plugin-[your-plugin-name]`
3. Create new directory under the plugins directory. The name must be unique amongst all plugins and should be lowercase containing letters, numbers or dashes.
4. In the directory created in #3, create a new file called plugin.yaml
5. Populate your plugin.yaml file with the following


**Name and description - This will be displayed in the plugin catalog**
```
name: Plugin Name
description: Collect, monitor and alert on packetloss statistics.
```

**Documentation - A link to documentation for your plugin should also be provided and will be linked to in the VNS3 catalog**
```
documentation: https://docs.cohesive.net/docs/network-edge-plugins/overlay-engine/
```

**Image url or instructions on how to attain an image** - One of image_url or setup_url should be provided. Ideally an image url can be provided such that VNS3 can immediately install your plugin. If instead you require a workflow whereby a client must first sign up with your service before being able to download a VNS3 plugin, the setup_url should be used linking to how to acquire this plugin for download.
```
image_url: https://vns3-containers-read-all.s3.amazonaws.com/Overlayengine/overlayengine_20200510.tar.gz
setup_url: https://how.to.setup.com
```

**Categories** - a list of categories in which your plugin falls
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

If your plugin does not fall into one of the provided categories and would like to suggest a new category, feel free to put a pull request into this repo editing this README.md. Please create a branch called `add-category-[new category]` for your pull request.

## Installing
All plugins in master will be displayed in VNS3 on the install plugins page.


![Install page picture](https://vns3-testing-assets.s3.amazonaws.com/vns3-plugin-install-page.png "VNS3 plugin install page")
