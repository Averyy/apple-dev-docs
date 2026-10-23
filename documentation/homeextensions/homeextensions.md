# HomeExtensions

**Framework**: HomeExtensions  
**Kind**: module  
**Role**: Framework

Add custom UI to the Home app, to configure and control accessories.

#### Overview

Use the Home Extensions framework to make accessories that you manufacture available in the Home app for people to set up, control, and configure. You can provide accessory settings, create custom SwiftUI views for configuration, and offer supporting content.

> ❗ **Important**:  Home Extensions is available at compile time only. The framework’s functionality will be available at a later date.

To use this framework, add a new target in Xcode by selecting File > New > Target, and then choose Home Extension. If you’re configuring your project manually, do the following:

- Add the [`com.apple.developer.home`](../BundleResources/entitlements/com.apple.developer.home.md) entitlement to your app extension.
- Add the `EXAppExtensionAttributes` key in the Info pane in Xcode for your app extension. Its value is a dictionary with `EXExtensionPointIdentifier` as a key and `com.apple.Home.HomeExtension` as a value.
- Add the `NSHomeExtensionManufacturer` key in the Info pane in Xcode for your app. Its value is a string containing the accessory manufacturer’s name.

## Topics

### Essentials
- [protocol HomeExtension](./homeextension.md)
  A type that represents an app extension for the Home app.
- [class HomeContext](./homecontext.md)
  The context in which the Home app launches your extension, including the selected home and accessory.
- [class HomeNavigator](./homenavigator.md)
  An object that manages navigation for your extension’s content in the Home app.
### Displaying accessory configuration
- [protocol HomeAccessorySettingsProvider](./homeaccessorysettingsprovider.md)
  A type that reads and writes an accessory’s settings.
- [protocol HomeAccessorySettingsContainer](./homeaccessorysettingscontainer.md)
  A snapshot of an accessory’s settings and their current values.
- [struct AnyHomeAccessorySettingsContainer](./anyhomeaccessorysettingscontainer.md)
- [protocol HomeAccessorySettingsContext](./homeaccessorysettingscontext.md)
  A type that holds the resources that your settings provider needs to communicate with an accessory.
- [struct HomeAccessorySettings](./homeaccessorysettings.md)
  Accessory settings that your extension provides to the Home app.
- [struct HomeAccessoryConfiguration](./homeaccessoryconfiguration.md)
  Content that people use to configure an accessory.
### Defining accessory settings
- [protocol HomeAccessorySetting](./homeaccessorysetting.md)
  A type that represents a single accessory setting.
- [struct HomeAccessorySettingLabel](./homeaccessorysettinglabel.md)
  The text that the Home app displays for a setting or an option.
- [class HomeAccessoryEnumSetting](./homeaccessoryenumsetting.md)
  A setting that offers a choice among several options.
- [protocol HomeAccessoryEnumSettingConstant](./homeaccessoryenumsettingconstant.md)
  A type whose cases are the options for an enumeration setting.
- [class HomeAccessoryInformationSetting](./homeaccessoryinformationsetting.md)
  A read-only setting that displays a label and a value.
- [class HomeAccessoryRangeSetting](./homeaccessoryrangesetting.md)
  A setting that represents a numeric value within a range.
- [protocol HomeAccessoryRangeSettingDescriptor](./homeaccessoryrangesettingdescriptor.md)
  A type that describes the bounds of a range setting.
- [class HomeAccessoryTextFieldSetting](./homeaccessorytextfieldsetting.md)
  A setting that contains a single line of editable text.
- [class HomeAccessoryToggleSetting](./homeaccessorytogglesetting.md)
  A setting that offers a binary choice, such as on or off.
### Guides and troubleshooting content
- [protocol HomeContent](./homecontent.md)
  A type that represents content that your extension provides to the Home app.
- [struct HomeContentID](./homecontentid.md)
  An identifier for a piece of content that your extension provides.
- [struct HomeAccessoryHelpGuide](./homeaccessoryhelpguide.md)
  Help content about a specific topic for an accessory.
- [struct HomeAccessoryTroubleshooting](./homeaccessorytroubleshooting.md)
  Content that helps people resolve problems with an accessory.
- [class GuideStepHostViewController](./guidestephostviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions)*