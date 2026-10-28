# framework

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

A type that represents an Apple framework bundle.

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
static var framework: UTType { get }
```

## Discussion

The identifier for this type is `com.apple.framework`.

This type conforms to [`UTTypePluginBundle`](../uttypepluginbundle.md).

## See Also

### Apple system types
- [static var applicationBundle: UTType](./applicationbundle.md)
  A type that represents a bundled app.
- [static var applicationExtension: UTType](./applicationextension.md)
  A type that represents an app extension.
- [static var spotlightImporter: UTType](./spotlightimporter.md)
  A type that represents a Spotlight metadata importer bundle.
- [static var quickLookGenerator: UTType](./quicklookgenerator.md)
  A type that represents a QuickLook preview generator bundle.
- [static var xpcService: UTType](./xpcservice.md)
  A type that represents an XPC service bundle.
- [static var systemPreferencesPane: UTType](./systempreferencespane.md)
  A type that represents a System Preferences pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/framework)*