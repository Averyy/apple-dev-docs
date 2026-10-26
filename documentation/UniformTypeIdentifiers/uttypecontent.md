# UTTypeContent

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

A base type that represents anything containing user-viewable content.

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
extern UTType * const UTTypeContent;
```

#### Discussion

Types that conform to content include documents, pasteboard data, and document packages. Types describing files or packages must also conform to [`UTTypeData`](./uttypedata.md) or [`UTTypePackage`](./uttypepackage.md) in order for the system to bind documents to them.

The identifier for this type is `public.content`.

## See Also

### Apple system base types
- [UTTypeItem](./uttypeitem.md)
  A generic base type for most objects, such as files or directories.
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
- [UTTypeApplication](./uttypeapplication.md)
  A base type that represents a macOS, iOS, iPadOS, watchOS, and tvOS app.
- [UTTypeSourceCode](./uttypesourcecode.md)
  A base type that represents source code of any programming language.
- [UTTypeBookmark](./uttypebookmark.md)
  A base type that represents bookmark data.
- [UTTypeLog](./uttypelog.md)
  A base type that represents console log data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypecontent)*