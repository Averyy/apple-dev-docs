# FxPathAPI_v3

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

An API that defines the methods to retrieve information about paths, shapes, and masks the user has drawn on an object.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxPathAPI_v3
```

```objc
@protocol FxPathAPI_v3
```

## Overview

This API is used to get information about a path that the user has drawn on an object in the canvas. You can get the number of paths applied to the object, and then enumerate through them, or pick a specific one. You can use this API to retrieve the control points along the path and use that information to guide the rendering of your plug-in.

> **Note**:  This API does not inherit from the `FxPathAPI`. It is a new API for FxPlug 4 that uses [`CMTime`](../CoreMedia/cmtime.md) and handles `NSErrors` consistently with other familiar APIs.

## Topics

### Getting Path Information
- [func numberOfPaths(at: CMTime) -> Int](./fxpathapi_v3/numberofpaths%28at%29.md)
  Provides the number of paths on the object to which your filter is applied, or on your generator.
- [func pathID(UnsafeMutablePointer<FxPathID?>!, for: Int) throws](./fxpathapi_v3/pathid%28_,for%29.md)
  Gets the unique ID of the path at the index requested.
- [func name(AutoreleasingUnsafeMutablePointer<NSString?>!, ofPath: FxPathID!) throws](./fxpathapi_v3/name%28_,ofpath%29.md)
  Provides the name the user has entered for the path with the given ID.
- [func isPath(FxPathID!, open: UnsafeMutablePointer<ObjCBool>!, at: CMTime) throws](./fxpathapi_v3/ispath%28_,open,at%29.md)
  Tells whether the path is opened or closed.
- [func isPath(FxPathID!, inverted: UnsafeMutablePointer<ObjCBool>!, at: CMTime) throws](./fxpathapi_v3/ispath%28_,inverted,at%29.md)
  Tells whether the path is inverted or not.
- [func style(UnsafeMutablePointer<FxPathStyle>!, ofPath: FxPathID!) throws](./fxpathapi_v3/style%28_,ofpath%29.md)
  Provides the style of the path — linear, bezier, or b-spline.
- [func length(UnsafeMutablePointer<Double>!, ofPath: FxPathID!, at: CMTime) throws](./fxpathapi_v3/length%28_,ofpath,at%29.md)
  Provides you the length of the entire path.
- [func length(UnsafeMutablePointer<Double>!, ofSegment: Int, ofPath: FxPathID!, at: CMTime) throws](./fxpathapi_v3/length%28_,ofsegment,ofpath,at%29.md)
  Provides the length of one segment of the entire path.
- [func number(ofVertices: UnsafeMutablePointer<Int>!, inPath: FxPathID!, at: CMTime) throws](./fxpathapi_v3/number%28ofvertices,inpath,at%29.md)
  Provides the number of vertices in the given path at the given time.
- [func vertex(UnsafeMutablePointer<FxVertex>!, at: Int, ofPath: FxPathID!, at: CMTime) throws](./fxpathapi_v3/vertex%28_,at,ofpath,at%29.md)
  Provides information about a single vertex on the path at the given time.
- [func point(UnsafeMutablePointer<FxPoint2D>!, atPercentageOfDistance: Double, alongPath: FxPathID!, at: CMTime) throws](./fxpathapi_v3/point%28_,atpercentageofdistance,alongpath,at%29.md)
  Provides a 2D point that contains the location of the point on the path, at a distance along the path’s length  equal to the value of `percentDist`.
- [func point(UnsafeMutablePointer<FxPoint2D>!, atPercentageOfParameter: Double, alongPath: FxPathID!, at: CMTime) throws](./fxpathapi_v3/point%28_,atpercentageofparameter,alongpath,at%29.md)
  Provides a 2D point that contains the location of the point on the path, at a distance along the path’s parametric distance equal to the percent value of `percentParameter`.
- [func blendMode(UnsafeMutablePointer<FxPathBlendMode>!, ofPath: FxPathID!) throws](./fxpathapi_v3/blendmode%28_,ofpath%29.md)
  Gets the blending mode for a given path.
- [func pathGeometryInfo(UnsafeMutablePointer<FxPathGeometryInfo>!, forPath: FxPathID!, at: CMTime) throws](./fxpathapi_v3/pathgeometryinfo%28_,forpath,at%29.md)
  Gets geometry information about a given path.
### Setting Path Information
- [func setPath(FxPathID!, toColor: FxPathColor) throws](./fxpathapi_v3/setpath%28_,tocolor%29.md)
  Sets the color the host app uses to draw the path with the given ID.
### Structuring Path Information
- [struct FxPathGeometryInfo](./fxpathgeometryinfo.md)
  A structure that defines the geometry information of the path.
- [struct FxVertex](./fxvertex.md)
  The properties of one vertex in a path.
### Constants
- [typealias FxPathBlendMode](./fxpathblendmode.md)
  The type of blending the user selects for the mask that a particular path describes.
- [typealias FxPathColor](./fxpathcolor.md)
  The colors that the host app uses to display a path.
- [typealias FxPathID](./fxpathid.md)
  The unique identifier for a path.
- [typealias FxPathStyle](./fxpathstyle.md)
  The style of the path, which is linear, bezier, or b-spline.

## See Also

### User interface
- [Adding parameters to plug-ins](../Professional-Video-Applications/adding-parameters-to-plug-ins.md)
  Create standard and custom user-facing parameters for your plug-in that will appear in the inspector.
- [Adding onscreen controls to plug-ins](../Professional-Video-Applications/adding-onscreen-controls-to-plug-ins.md)
  Simplify user interaction by using onscreen controls for your FxPlug plug-in.
- [protocol FxUndoAPI](./fxundoapi.md)
  An API that defines the methods that the host app implements to handle plug-in management of the host app’s undo queue.
- [protocol FxCommandAPI](./fxcommandapi.md)
  Commands that you can tell the host to perform.
- [protocol FxCommandAPI_v2](./fxcommandapi_v2.md)
  Adds functionality to move the playhead to a specific timeline time.
- [protocol FxRemoteWindowAPI](./fxremotewindowapi.md)
  A protocol that allows the plug-in to request that the host create a window.
- [protocol FxRemoteWindowAPI_v2](./fxremotewindowapi_v2.md)
  A protocol that allows the plug-in to request that the host create a window with a defined minimum and maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxpathapi_v3)*