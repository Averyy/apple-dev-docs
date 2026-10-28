# hvf

**Framework**: hvf  
**Kind**: module  
**Role**: Framework

Render Hierarchical Variable Font (HVF) glyph outlines, and support font editors and related tools.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Overview

The `hvf` library provides C and Swift interfaces. The C interface supports rendering `hvgl` and `hvpm` tables in existing fonts.

The Swift interface adds support for the following:

- Writing a custom loader to render HVF glyphs from other sources, such as a database in a font editor.
- Generating data needed to build an `hvgl` table, using the same code as the custom loader.
- Interactively modifying part appearances and data, such as in a font editor.

## Topics

### Classes
- [class HVGLPartLoader](./hvglpartloader.md)
  Special loader object for an HVGL table in memory, which must be Double-aligned Typically this is from a memory-mapped font
- [class PartRenderer](./partrenderer.md)
  An object that can be used to set parameters for rendering a part, to render the part, and to diagnose the results of rendering
### Protocols
- [protocol CompositeWriter](./compositewriter.md)
  Protocol for creating a Composite part for rendering or to build an HVGL table
- [protocol PartGenerator](./partgenerator.md)
  Protocol for returning a writer object to create Shape or Composite data
- [protocol ShapeWriter](./shapewriter.md)
  A protocol for creating a Shape part for rendering or to build an HVGL table
### Structures
- [struct CompositeExtremumIndex](./compositeextremumindex.md)
  The index of an extremum rotation or translation in a Composite part
- [struct CompositeSubpart](./compositesubpart.md)
  A subpart in a Composite part
- [struct CompositeSubpartTranslation](./compositesubparttranslation.md)
  A subpart translation in a Composite part
- [HVFLibraryVersion](./hvflibraryversion-c.struct.md)
  The type used for the version of the hvf library.
- [HVFPartInfo](./hvfpartinfo.md)
  The type used for part information that is passed from the scaler to the callback.
- [HVFPoint](./hvfpoint.md)
  The type of a single 2D point passed from the scaler to the callback.
- [HVFTableVersion](./hvftableversion.md)
  The type used for the `hvgl` table version supported by this version of the hvf library.
- [HVFTranslation](./hvftranslation.md)
  The type of a 2D translation passed to the scaler.
### Variables
- [let hvfLibraryVersion: (major: Int, minor: Int, patch: Int)](./hvflibraryversion-swift.var.md)
  Return the version of the HVF library
### Type Aliases
- [typealias CustomPartLoader](./custompartloader.md)
  Closure which loads parts from an arbitrary source The first parameter is the part index which uniquely identifiers a part; these are assigned by the loader The second parameter is a PartGenerator the loader uses to get a ShapeWriter or CompositeWriter to create the requested part The result is the generated part, passed back in a PartResult
- [HVFAxisValue](./hvfaxisvalue.md)
  A value that can be set on an axis.
- [HVFPartIndex](./hvfpartindex.md)
  Index of a part within an `hvgl` table or other source.
- [HVFRenderContext](./hvfrendercontext.md)
  The type of the callback passed to `HVF_render_current_part()`.
- [HVFRotation](./hvfrotation.md)
  The type of a rotation passed to the scaler.
- [HVFXYCoord](./hvfxycoord.md)
  The type used for 2D x and y coordinates.
### Enumerations
- [enum AxisExtremum](./axisextremum.md)
  Which extremum within an axis
- [enum PartResult](./partresult.md)
  The result returned from a part loader
- [enum PointCoordinate](./pointcoordinate.md)
  Which coordinate within a point
- [enum SegmentBlendType](./segmentblendtype.md)
  The blend type for a segment of a path
- [enum SegmentPoint](./segmentpoint.md)
  Which point within a segment
- [HVFPartRenderAction](./hvfpartrenderaction.md)
  Actions that a render context may return to the scaler.
- [HVFPartRenderInstruction](./hvfpartrenderinstruction.md)
  Instruction passed by the scaler to a callback. Some of the instructions have associated data described by the `HVFPartRenderParams` union.
### Unions
- [HVFPartRenderParameters](./hvfpartrenderparameters.md)
  A union type describing associated data values for cases of `HVFPartRenderInstruction`.
### Functions
- [HVF_clear_part_cache](./hvf_clear_part_cache.md)
  Clear the cache of loaded parts.
- [HVF_close_part_renderer](./hvf_close_part_renderer.md)
  Reclaim any subsidiary storage used by the renderer and destroy it.
- [HVF_glyph_count](./hvf_glyph_count.md)
  Returns the number of glyphs (suitable for rendering) in the `hvgl` table.
- [HVF_library_version](./hvf_library_version.md)
  Return the version of the hvf library.
- [HVF_open_part_renderer](./hvf_open_part_renderer.md)
  Create a part renderer in the storage provided.
- [HVF_part_count](./hvf_part_count.md)
  Return the number of parts in the `hvgl` table.
- [HVF_part_renderer_storage_size](./hvf_part_renderer_storage_size.md)
  Return the storage that must be allocated for a part renderer.
- [HVF_render_current_part](./hvf_render_current_part.md)
  Render the current part using the supplied callback.
- [HVF_render_part_axis_count](./hvf_render_part_axis_count.md)
  Return the number of axes for the current part, or -1 if the part is not set.
- [HVF_set_axis_value](./hvf_set_axis_value.md)
  Set the axis value.
- [HVF_set_render_part](./hvf_set_render_part.md)
  Set the renderer to render the part indicated by the part index.
- [HVF_table_version](./hvf_table_version.md)
  Return the `hvgl` table version supported by the scaler code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf)*