# HomeContentID

**Framework**: HomeExtensions  
**Kind**: struct  
**Role**: Structure

An identifier for a piece of content that your extension provides.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct HomeContentID
```

#### Overview

Defining identifiers as constants, instead of using strings, lets you reuse them and avoid typos. For example:

```swift
extension HomeContentID {
    static let batteryGuide: HomeContentID = "battery-guide"
}

HomeAccessoryHelpGuide(id: .batteryGuide) {
    BatteryGuideView()
}
```

You can also use a string literal anywhere an identifier is expected.

## Topics

### Creating a content identifier
- [init(String)](./homecontentid/init%28_%29.md)
  Creates an identifier from a string.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Guides and troubleshooting content
- [protocol HomeContent](./homecontent.md)
  A type that represents content that your extension provides to the Home app.
- [struct HomeAccessoryHelpGuide](./homeaccessoryhelpguide.md)
  Help content about a specific topic for an accessory.
- [struct HomeAccessoryTroubleshooting](./homeaccessorytroubleshooting.md)
  Content that helps people resolve problems with an accessory.
- [class GuideStepHostViewController](./guidestephostviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homecontentid)*