# HomeContent

**Framework**: HomeExtensions  
**Kind**: protocol  
**Role**: Protocol

A type that represents content that your extension provides to the Home app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
protocol HomeContent
```

## Overview

Don’t add new conforming types.  Use the types from this framework, such as [`HomeAccessoryConfiguration`](./homeaccessoryconfiguration.md), [`HomeAccessorySettings`](./homeaccessorysettings.md), [`HomeAccessoryHelpGuide`](./homeaccessoryhelpguide.md), and [`HomeAccessoryTroubleshooting`](./homeaccessorytroubleshooting.md) in your [`body`](./homeextension/body.md) property.

## Relationships

### Conforming Types
- [HomeAccessoryConfiguration](./homeaccessoryconfiguration.md)
- [HomeAccessoryHelpGuide](./homeaccessoryhelpguide.md)
- [HomeAccessorySettings](./homeaccessorysettings.md)
- [HomeAccessoryTroubleshooting](./homeaccessorytroubleshooting.md)

## See Also

### Guides and troubleshooting content
- [struct HomeContentID](./homecontentid.md)
  An identifier for a piece of content that your extension provides.
- [struct HomeAccessoryHelpGuide](./homeaccessoryhelpguide.md)
  Help content about a specific topic for an accessory.
- [struct HomeAccessoryTroubleshooting](./homeaccessorytroubleshooting.md)
  Content that helps people resolve problems with an accessory.
- [class GuideStepHostViewController](./guidestephostviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homecontent)*