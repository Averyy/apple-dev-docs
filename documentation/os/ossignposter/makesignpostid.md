# makeSignpostID()

**Framework**: os  
**Kind**: method

Returns an identifier that’s unique within the scope of the signposter.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func makeSignpostID() -> OSSignpostID
```

## Mentions

- [Recording Performance Data](recording-performance-data.md)

#### Return Value

A signpost ID that you use to match an interval’s signposts.

#### Discussion

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously.

Use this method instead of [`init(log:)`](ossignpostid/init(log:).md).

## See Also

- [func makeSignpostID(from: AnyObject) -> OSSignpostID](ossignposter/makesignpostid(from:).md)
  Returns an identifier that the signposter derives from the specified object.
- [struct OSSignpostID](ossignpostid.md)
  An identifier that disambiguates signposted intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/makesignpostid())*