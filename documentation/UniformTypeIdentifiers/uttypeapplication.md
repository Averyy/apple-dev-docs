# UTTypeApplication

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

A base type that represents a macOS, iOS, iPadOS, watchOS, and tvOS app.

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
extern UTType * const UTTypeApplication;
```

## Discussion

The identifier for this type is `com.apple.application`.

This type conforms to [`UTTypeExecutable`](./uttypeexecutable.md).

## See Also

### Apple system base types
- [UTTypeItem](./uttypeitem.md)
  A generic base type for most objects, such as files or directories.
- [UTTypeContent](./uttypecontent.md)
  A base type that represents anything containing user-viewable content.
- [UTTypeCompositeContent](./uttypecompositecontent.md)
  A base type that represents a content format supporting mixed embedded content.
- [UTTypeData](./uttypedata.md)
  A base type that represents any sort of byte stream, including files and in-memory data.
- [UTTypeResolvable](./uttyperesolvable.md)
  A base type that represents a resolvable reference, including symbolic links and aliases.
- [UTTypePackage](./uttypepackage.md)
  A base type that represents a packaged directory.
- [UTTypeBundle](./uttypebundle.md)
  A base type that represents a directory that conforms to one of the bundle layouts.
- [UTTypePluginBundle](./uttypepluginbundle.md)
  A base type that represents a bundle-based plug-in.
- [UTTypeSourceCode](./uttypesourcecode.md)
  A base type that represents source code of any programming language.
- [UTTypeBookmark](./uttypebookmark.md)
  A base type that represents bookmark data.
- [UTTypeLog](./uttypelog.md)
  A base type that represents console log data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeapplication)*