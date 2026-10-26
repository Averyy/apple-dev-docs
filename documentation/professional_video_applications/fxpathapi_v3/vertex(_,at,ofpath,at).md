# vertex(_:at:ofPath:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides information about a single vertex on the path at the given time.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func vertex(_ vertex: UnsafeMutablePointer<FxVertex>!, at index: Int, ofPath pathID: FxPathID!, at time: CMTime) throws
```

```objc
- (BOOL) vertex:(FxVertex *) vertex atIndex:(NSUInteger) index ofPath:(FxPathID) pathID atTime:(CMTime) time error:(NSError * *) err;
```

## Parameters

- `vertex`: A pointer to an FxVertex structure to hold the information about the vertex in question.
- `index`: The index of the vertex you want to retrieve. This is `0`-based, so if the path has `n` vertices, this will be between `0` and `n-1`.
- `pathID`: The ID of the path from which you wish to retrieve a vertex.
- `time`: The time at which to retrieve the vertex information.

## See Also

### Getting Path Information
- [func numberOfPaths(at: CMTime) -> Int](./numberofpaths%28at%29.md)
  Provides the number of paths on the object to which your filter is applied, or on your generator.
- [func pathID(UnsafeMutablePointer<FxPathID?>!, for: Int) throws](./pathid%28_,for%29.md)
  Gets the unique ID of the path at the index requested.
- [func name(AutoreleasingUnsafeMutablePointer<NSString?>!, ofPath: FxPathID!) throws](./name%28_,ofpath%29.md)
  Provides the name the user has entered for the path with the given ID.
- [func isPath(FxPathID!, open: UnsafeMutablePointer<ObjCBool>!, at: CMTime) throws](./ispath%28_,open,at%29.md)
  Tells whether the path is opened or closed.
- [func isPath(FxPathID!, inverted: UnsafeMutablePointer<ObjCBool>!, at: CMTime) throws](./ispath%28_,inverted,at%29.md)
  Tells whether the path is inverted or not.
- [func style(UnsafeMutablePointer<FxPathStyle>!, ofPath: FxPathID!) throws](./style%28_,ofpath%29.md)
  Provides the style of the path — linear, bezier, or b-spline.
- [func length(UnsafeMutablePointer<Double>!, ofPath: FxPathID!, at: CMTime) throws](./length%28_,ofpath,at%29.md)
  Provides you the length of the entire path.
- [func length(UnsafeMutablePointer<Double>!, ofSegment: Int, ofPath: FxPathID!, at: CMTime) throws](./length%28_,ofsegment,ofpath,at%29.md)
  Provides the length of one segment of the entire path.
- [func number(ofVertices: UnsafeMutablePointer<Int>!, inPath: FxPathID!, at: CMTime) throws](./number%28ofvertices,inpath,at%29.md)
  Provides the number of vertices in the given path at the given time.
- [func point(UnsafeMutablePointer<FxPoint2D>!, atPercentageOfDistance: Double, alongPath: FxPathID!, at: CMTime) throws](./point%28_,atpercentageofdistance,alongpath,at%29.md)
  Provides a 2D point that contains the location of the point on the path, at a distance along the path’s length  equal to the value of `percentDist`.
- [func point(UnsafeMutablePointer<FxPoint2D>!, atPercentageOfParameter: Double, alongPath: FxPathID!, at: CMTime) throws](./point%28_,atpercentageofparameter,alongpath,at%29.md)
  Provides a 2D point that contains the location of the point on the path, at a distance along the path’s parametric distance equal to the percent value of `percentParameter`.
- [func blendMode(UnsafeMutablePointer<FxPathBlendMode>!, ofPath: FxPathID!) throws](./blendmode%28_,ofpath%29.md)
  Gets the blending mode for a given path.
- [func pathGeometryInfo(UnsafeMutablePointer<FxPathGeometryInfo>!, forPath: FxPathID!, at: CMTime) throws](./pathgeometryinfo%28_,forpath,at%29.md)
  Gets geometry information about a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxpathapi_v3/vertex(_:at:ofpath:at:))*