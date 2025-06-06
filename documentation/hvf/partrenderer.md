# PartRenderer

**Framework**: hvf  
**Kind**: class

An object that can be used to set parameters for rendering a part, to render the part, and to diagnose the results of rendering

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class PartRenderer
```

## Topics

### Classes
- [PartRenderer.AxisValues](partrenderer/axisvalues.md)
  All the axis values applied to a part. The index is the axis number (determined by the loader). Axis values are in design space (-1.0…1.0)
- [PartRenderer.PartParameters](partrenderer/partparameters.md)
  All the parameters applied to a part, including nested subparts
### Structures
- [PartRenderer.Point](partrenderer/point.md)
  A point returned from the scaler
- [PartRenderer.Subparts](partrenderer/subparts.md)
  Collection of part parameters for the subparts of a part. The index is the subpart number (determined by the loader)
- [PartRenderer.Translation](partrenderer/translation.md)
  A translation applied to a subpart
### Initializers
- [init(custom: CustomPartLoader, reusable: Bool)](partrenderer/init(custom:reusable:).md)
  Use a custom, client-defined loader Setting reusable to true preserves the input parameter values when rendering; otherwise they are destroyed by rendering
- [init(hvglLoader: HVGLPartLoader, reusable: Bool)](partrenderer/init(hvglloader:reusable:).md)
  Use a loader specific to an HVGL table in memory Setting reusable to true preserves the input parameter values when rendering; otherwise they are destroyed by rendering
### Instance Properties
- [var blendedAxisValueBounds: ClosedRange<Double>](partrenderer/blendedaxisvaluebounds.md)
  After rendering, returns the maximum and minimum blended values set on any axis in the part’s tree This is useful for detecting axes going out of range (-1.0…1.0)
- [var parameters: PartRenderer.PartParameters](partrenderer/parameters.md)
  Parameters that control how the part is rendered. The default is to set all axes, rotations, translations, etc. to zero
- [var partAxisCount: Int](partrenderer/partaxiscount.md)
  The number of axes of the current part; zero if no part set
- [var partIndex: Int](partrenderer/partindex.md)
  The unique identifier of the part to be rendered. Setting this resets the parameters property to default values (an empty part parameter tree). Any previously captured PartParameters or AxisValues are invalid.
### Instance Methods
- [func clearPartCache()](partrenderer/clearpartcache.md)
  Clear the cache of loaded parts. This only happens when this function is called.
- [func render(to: (PartRenderer.Instruction) -> PartRenderer.Action) -> Bool](partrenderer/render(to:).md)
  Render the current part using the current parameters using the supplied render context If the PartRenderer was created using reusable, all input parameters are intact afterwards; otherwise they are destroyed Returns true if rendering was successful
### Enumerations
- [PartRenderer.Action](partrenderer/action.md)
  Action requested by the render context after processing an instruction
- [PartRenderer.Instruction](partrenderer/instruction.md)
  The set of instructions passed to a render context


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer)*