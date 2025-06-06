# makeSignpostID(from:)

**Framework**: os  
**Kind**: method

Returns an identifier that the signposter derives from the specified object.

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
func makeSignpostID(from object: AnyObject) -> OSSignpostID
```

#### Return Value

A signpost ID that you use to match an interval’s signposts.

#### Discussion

> ⚠️ **Warning**:  Don’t use this method to generate an identifier for a signposted interval that crosses process boundaries. Instead, use the [`makeSignpostID()`](ossignposter/makesignpostid().md) method.

 Don’t use this method to generate an identifier for a signposted interval that crosses process boundaries. Instead, use the [`makeSignpostID()`](ossignposter/makesignpostid().md) method.

The signposter uses a signpost ID to pair the beginning and the end of a signposted interval, which is necessary because multiple intervals with the same configuration and scope can be in-flight simultaneously.

Use this method instead of [`init(log:object:)`](ossignpostid/init(log:object:).md).

## Parameters

- `object`: The object the signposter uses to match the begin and end calls of a signposted interval.

## See Also

- [func makeSignpostID() -> OSSignpostID](ossignposter/makesignpostid.md)
  Returns an identifier that’s unique within the scope of the signposter.
- [struct OSSignpostID](ossignpostid.md)
  An identifier that disambiguates signposted intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/ossignposter/makesignpostid(from:))*