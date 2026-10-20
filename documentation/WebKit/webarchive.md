# WebArchive

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

A WebArchive object represents a webpage that can be archived—for example, archived on disk or on the pasteboard. A WebArchive object contains the main resource, as well as the subresources and subframes of the main resource. The main resource can be an entire webpage, a portion of a webpage, or some other kind of data such as an image. Use this class to archive webpages, or place a portion of a webpage on the pasteboard, or to represent rich web content in any application.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
class WebArchive
```

```objc
@interface WebArchive : NSObject
```

## Topics

### Initializing
- [init!(mainResource: WebResource!, subresources: [Any]!, subframeArchives: [Any]!)](./webarchive/init%28mainresource,subresources,subframearchives%29.md)
  Initializes the receiver with a resource and optional subresources and subframe archives..
- [init!(data: Data!)](./webarchive/init%28data%29.md)
  Initializes and returns the receiver, specifying the initial content data.
### Getting attributes
- [var mainResource: WebResource!](./webarchive/mainresource.md)
  The receiver’s main resource.
- [var subresources: [Any]!](./webarchive/subresources.md)
  The receiver’s subresources, or `nil` if there are none.
- [var subframeArchives: [Any]!](./webarchive/subframearchives.md)
  Archives representing the receiver’s subresources or `nil` if there are none.
- [var data: Data!](./webarchive/data.md)
  The data representation of the receiver.
### Constants
- [let WebArchivePboardType: String](./webarchivepboardtype.md)
  The pasteboard type constant used when adding or accessing a WebArchive on the pasteboard.
### Initializers
- [init?(coder: NSCoder)](./webarchive/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webarchive)*