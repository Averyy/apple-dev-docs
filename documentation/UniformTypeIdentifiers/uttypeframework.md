# UTTypeFramework

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

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

```c
extern UTType * const UTTypeFramework;
```

## Discussion

The identifier for this type is `com.apple.framework`.

This type conforms to [`UTTypeBundle`](./uttypebundle.md).

## See Also

### Apple system types
- [UTTypeApplicationBundle](./uttypeapplicationbundle.md)
  A type that represents a bundled app.
- [UTTypeApplicationExtension](./uttypeapplicationextension.md)
  A type that represents an app extension.
- [UTTypeSpotlightImporter](./uttypespotlightimporter.md)
  A type that represents a Spotlight metadata importer bundle.
- [UTTypeQuickLookGenerator](./uttypequicklookgenerator.md)
  A type that represents a QuickLook preview generator bundle.
- [UTTypeXPCService](./uttypexpcservice.md)
  A type that represents an XPC service bundle.
- [UTTypeSystemPreferencesPane](./uttypesystempreferencespane.md)
  A type that represents a System Preferences pane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeframework)*