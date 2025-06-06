# xpcService

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type that represents an XPC service bundle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var xpcService: UTType { get }
```

#### Discussion

The identifier for this type is `com.apple.xpc-service`.

This type conforms to [`UTTypeBundle`](uttypebundle.md) and [`UTTypePackage`](uttypepackage.md).

## See Also

- [static var framework: UTType](uttype-swift.struct/framework.md)
  A type that represents an Apple framework bundle.
- [static var applicationBundle: UTType](uttype-swift.struct/applicationbundle.md)
  A type that represents a bundled app.
- [static var applicationExtension: UTType](uttype-swift.struct/applicationextension.md)
  A type that represents an app extension.
- [static var spotlightImporter: UTType](uttype-swift.struct/spotlightimporter.md)
  A type that represents a Spotlight metadata importer bundle.
- [static var quickLookGenerator: UTType](uttype-swift.struct/quicklookgenerator.md)
  A type that represents a QuickLook preview generator bundle.
- [static var systemPreferencesPane: UTType](uttype-swift.struct/systempreferencespane.md)
  A type that represents a System Preferences pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/xpcservice)*