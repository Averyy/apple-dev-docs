# package

**Framework**: Uniform Type Identifiers  
**Kind**: property

A base type that represents a packaged directory.

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
static var package: UTType { get }
```

#### Discussion

Bundles differ from packages in that a bundle has an internal file hierarchy that [`CFBundle`](https://developer.apple.com/documentation/CoreFoundation/CFBundle) can read, while packages display to the user as if they were regular files. A single file system object can be a package and a bundle.

The identifier for this type is `com.apple.package`.

This type conforms to [`UTTypeDirectory`](uttypedirectory.md).

## See Also

- [static var item: UTType](uttype-swift.struct/item.md)
  A generic base type for most objects, such as files or directories.
- [static var content: UTType](uttype-swift.struct/content.md)
  A base type that represents anything containing user-viewable content.
- [static var compositeContent: UTType](uttype-swift.struct/compositecontent.md)
  A base type that represents a content format supporting mixed embedded content.
- [static var data: UTType](uttype-swift.struct/data.md)
  A base type that represents any sort of byte stream, including files and in-memory data.
- [static var resolvable: UTType](uttype-swift.struct/resolvable.md)
  A base type that represents a resolvable reference, including symbolic links and aliases.
- [static var bundle: UTType](uttype-swift.struct/bundle.md)
  A base type that represents a directory that conforms to one of the bundle layouts.
- [static var pluginBundle: UTType](uttype-swift.struct/pluginbundle.md)
  A base type that represents a bundle-based plug-in.
- [static var application: UTType](uttype-swift.struct/application.md)
  A base type that represents a macOS, iOS, iPadOS, watchOS, and tvOS app.
- [static var sourceCode: UTType](uttype-swift.struct/sourcecode.md)
  A base type that represents source code of any programming language.
- [static var bookmark: UTType](uttype-swift.struct/bookmark.md)
  A base type that represents bookmark data.
- [static var log: UTType](uttype-swift.struct/log.md)
  A base type that represents console log data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/package)*