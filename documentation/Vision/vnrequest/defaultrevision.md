# defaultRevision

**Framework**: Vision  
**Kind**: property  
**Role**: Type Property

The revision of the latest request for the particular SDK linked with the client application.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class var defaultRevision: Int { get }
```

```objc
@property (class, nonatomic, assign, readonly) NSUInteger defaultRevision;
```

## See Also

### Determining the Revision
- [protocol VNRequestRevisionProviding](../vnrequestrevisionproviding.md)
  A protocol for specifying the revision number of Vision algorithms.
- [class var currentRevision: Int](./currentrevision.md)
  The current revison supported by the request.
- [class var supportedRevisions: IndexSet](./supportedrevisions.md)
  The collection of currently-supported algorithm versions for the class of request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequest/defaultrevision)*