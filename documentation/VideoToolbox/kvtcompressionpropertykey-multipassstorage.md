# kVTCompressionPropertyKey_MultiPassStorage

**Framework**: Videotoolbox  
**Kind**: var

A property key that enables multipass compression and provides storage for encoder private data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_MultiPassStorage: CFString
```

#### Discussion

Some video encoders support multipass encoding.  To determine whether a [`VTCompressionSession`](vtcompressionsession-api-collection.md) supports multipass encoding, you can inspect the dictionary returned by [`VTSessionCopySupportedPropertyDictionary(_:supportedPropertyDictionaryOut:)`](vtsessioncopysupportedpropertydictionary(_:supportedpropertydictionaryout:).md) to see if it contains [`kVTCompressionPropertyKey_MultiPassStorage`](kvtcompressionpropertykey_multipassstorage.md).

To enable multipass encoding, set the [`kVTCompressionPropertyKey_MultiPassStorage`](kvtcompressionpropertykey_multipassstorage.md) property to a [`VTMultiPassStorage`](vtmultipassstorage-api-collection.md) object, which you can create by calling [`VTMultiPassStorageCreate(allocator:fileURL:timeRange:options:multiPassStorageOut:)`](vtmultipassstoragecreate(allocator:fileurl:timerange:options:multipassstorageout:).md).  Then make one or more passes over the source frames.  Bracket each pass with a call to [`VTCompressionSessionBeginPass(_:flags:_:)`](vtcompressionsessionbeginpass(_:flags:_:).md) at the beginning and [`VTCompressionSessionEndPass(_:furtherPassesRequestedOut:_:)`](vtcompressionsessionendpass(_:furtherpassesrequestedout:_:).md) at the end.

In the first pass of multipass encoding, call [`VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)`](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md) for every source frame (just as in single-pass encoding).  At the end of every pass, call [`VTCompressionSessionEndPass(_:furtherPassesRequestedOut:_:)`](vtcompressionsessionendpass(_:furtherpassesrequestedout:_:).md).  This may take some time as the video encoder determines whether it can improve the encoding by performing another pass.  If the user cancels encoding during this time, call [`VTCompressionSessionInvalidate(_:)`](vtcompressionsessioninvalidate(_:).md) to interrupt the processing.  [`VTCompressionSessionEndPass(_:furtherPassesRequestedOut:_:)`](vtcompressionsessionendpass(_:furtherpassesrequestedout:_:).md) indicates through the `furtherPassesRequestedOut` argument whether the video encoder has requested another pass.  There is no particular limit on the number of passes the video encoder may request, but the client is free to disregard this request and use the last-emitted set of frames.

If `furtherPassesRequestedOut` is set to [`true`](https://developer.apple.com/documentation/swift/true) and you want to perform another pass, call [`VTCompressionSessionGetTimeRangesForNextPass(_:timeRangeCountOut:timeRangeArrayOut:)`](vtcompressionsessiongettimerangesfornextpass(_:timerangecountout:timerangearrayout:).md) to determine the time ranges for the next pass.  Only the source frames within these time ranges need to be passed to [`VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)`](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md); the video encoder is satisfied with the already-emitted compressed frames outside these ranges, and they can be kept for the final output.

In second and successive passes, you must pass identical source frames, frame properties, and timestamps to [`VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)`](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md) as in the first pass, with the exception that frames not in the requested time ranges should be skipped.

You can create and use a [`VTFrameSilo`](vtframesilo-api-collection.md) object to merge sequences of compressed frames across passes during multipass encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_multipassstorage)*