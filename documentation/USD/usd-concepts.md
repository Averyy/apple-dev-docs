# USD concepts

**Framework**: USD

Learn the core terms and ideas behind Universal Scene Description (USD).

#### Overview

Universal Scene Description (USD) is an open standard for describing, composing, and exchanging 3D scenes. It powers the entire Apple 3D pipeline — from Reality Composer Pro to the Preview app — and is the foundation of `.usdz`, `.usda`, and `.usdc` files. USD’s core strength is *composition*: you can layer multiple files together, apply overrides, and combine datasets without modifying the originals.

This article introduces the key concepts behind USD. Understanding these ideas helps you author USD files that render as expected, build efficient 3D assets, and diagnose problems when a scene doesn’t look right.

#### Scene Structure

##### Stage

A stage is the complete, resolved view of a USD scene. When you open a USD file, the system assembles all referenced layers and evaluates all composition rules to produce a single unified scene — that is the stage.

##### Layer

A layer is a single USD file or data source (`.usd`, `.usda`, `.usdc`, `.usdz`, or other USD-readable scene formats). Layers hold raw scene description: prims, properties, metadata, and composition rules. Multiple layers combine into a stage, and each layer only needs to describe what it contributes.

Layers also carry their own metadata. A stage applies metadata only from the *root layer* to all layers that compose that stage. Layer metadata includes:

- **defaultPrim** — the prim to use as the root when another file references this layer without specifying a target path.
- **upAxis** — the axis that points “up” in the scene (`Y` or `Z`).
- **metersPerUnit** — the scale of the scene, expressed as how many meters one scene unit represents.
- **timeCodesPerSecond** and **framesPerSecond** — the timing rate for animated content.
- **startTimeCode** and **endTimeCode** — the playback range of the scene.
- **customLayerData** — a dictionary for any custom key-value data you want to associate with the layer.

A layer stack is an ordered list of layers combined as if they were one. Layers higher in the stack take precedence over layers lower in the stack — similar to how layers work in a compositing application.

##### Namespace

The namespace is the hierarchical structure used to organize prims in a USD scene. Like a file system, the namespace arranges prims into a tree, and every prim has a unique path within it — for example, `/World/Characters/Hero`.

##### Path

A path is the address of a prim or property within the namespace, written as a slash-separated string such as `/Scene/Geometry/Cube`. When you reference an asset, USD automatically remaps any internal paths so they fit into your scene’s namespace.

##### Prim

A prim (short for *primitive*) is the basic building block of a USD scene. Every object — a mesh, a light, a camera, a material — is a prim. Prims form a hierarchy, and each prim can contain child prims, properties, and metadata. The schema defines the type of a prim.

When multiple layers each contribute data for the same prim, each layer’s contribution is called a *PrimSpec*. The ordered list of all PrimSpecs, from strongest to weakest layer, is the prim’s *prim stack*. Inspecting the prim stack helps you diagnose composition issues by showing exactly which layer provides each value.

##### Properties

A property is a named piece of data attached to a prim. There are two kinds:

- **Attributes** hold typed values — for example, the color of a material, the radius of a sphere, or the position of a transform. Attributes can store a single default value or a set of time-varying values. The type of an attribute is fixed (such as `float`, `color3f`, or `int[]`). Attributes can also be *connected* to each other — for example, connecting the output of one shader node to the input of another to form a material graph.
- **Relationships** point to one or more other prims or properties, identified by path. Unlike attributes, relationships don’t carry values — they express connections between objects. A material binding, for example, is a relationship from a mesh prim to a material prim. USD keeps relationship targets up-to-date when namespaces change due to referencing.

##### Metadata

Metadata is key-value data attached to a prim, property, or layer that describes the object rather than defining its visual appearance. For example, metadata can record the asset name, the tool version that created it, or custom user data. Metadata doesn’t vary over time. Common metadata keys include `kind`, `assetInfo`, `active`, and `customData`.

#### Composition

Composition is the process by which USD combines data from multiple layers into a single, unified stage. USD’s composition system lets you reference external assets, layer overrides, bundle variations, and share defaults — all without modifying the original files.

##### Composition Arcs

Composition arcs are the building blocks of USD’s composition system. Each arc creates a specific kind of relationship between layers or prims:

- **SubLayers** — stacks layers together, with earlier layers taking precedence. This is how you apply overrides across an entire scene.
- **References** — brings in a prim subtree from another layer and places it under a new path. This is the primary way to assemble scenes from reusable assets.
- **Payloads** — like references, but deferred: the system defers loading until you request it. Use payloads for large assets that should only load on demand.
- **Inherits** — links a derived prim to a base class prim, so changes to the class propagate to all inheritors. Useful for editing many instances of a type at once.
- **Specializes** — like inherits, but the derived prim’s opinions always win over the base. Use this when a variation should always be more specific than its source.
- **VariantSets** — bundles multiple variations into a single file, letting downstream users switch between them non-destructively.

When arcs contribute conflicting opinions for the same property, USD resolves the conflict using a strict precedence order: **Local → Inherits → VariantSets → References → Payloads → SubLayers**. Arcs earlier in the list take precedence over arcs later in the list.

##### Layer Offset

A layer offset shifts or scales the timing of time samples in a referenced layer. You can use it to offset an animation by a number of frames, or play it at a different speed, without touching the source file.

##### Flatten

Flattening a stage collapses all layers and composition arcs into a single, self-contained file with no external dependencies. The result is a snapshot of the scene as it currently appears. Flattening is useful for packaging a finished asset for delivery, but the output no longer carries the original composition structure.

##### Session Layer

The session layer is an in-memory layer at the top of the layer stack, giving it the highest opinion strength. It is ideal for temporary overrides — viewport selections, interactive adjustments, or per-session display settings — without writing them to disk.

#### Data Representation

##### Schema

A schema is a named template that defines the attributes, relationships, and metadata a prim should have. Schemas give prims their meaning. A mesh prim, for example, follows the `UsdGeomMesh` schema, which defines attributes like `points`, `faceVertexCounts`, and `subdivisionScheme`. There are two main kinds:

- **Typed schemas** define a prim’s type — `Mesh`, `Sphere`, `Camera`, and so on. Applying a typed schema changes what the prim fundamentally is.
- **API schemas** add a bundle of attributes or behaviors to an existing prim without changing its type. `PhysicsRigidBodyAPI`, for example, adds physics simulation attributes to any prim.

##### Def Class and Over

These three *specifiers* control how a prim is interpreted:

- **def** — a concrete prim that exists in the scene and is rendered or processed.
- **class** — a reusable template that isn’t rendered directly. Other prims can inherit from a class to pick up its values.
- **over** — an opinion about a prim defined elsewhere. An over only takes effect when a prim with the same path has a **def** in a weaker layer — an over layered on top of another over (with no underlying `def`) remains an over and never creates a concrete prim.

Because each layer stores its contribution to a prim independently — called a *prim spec* (short for *prim specifier*) — a prim’s specifier can differ from layer to layer. The stage composes these per-layer prim specs together, so a `def` in one layer and an `over` in a stronger layer combine into a single resolved prim.

##### Opinions and Default Values

An *opinion* is any value authored in a layer for a prim or property. When multiple layers contribute opinions for the same property, USD’s composition rules determine the winning value. A property with no time samples has a single authored value called its *default value*.

##### Time Samples and Animation

A time sample is a value for an attribute at a specific point in time. When an attribute has multiple time samples, it is animated — its value changes as time advances. You can use *splines* (mathematical curves) to interpolate smoothly between samples without storing a value at every frame.

Time is measured in *timecodes*, a unit independent of frame rate. The stage’s metadata records how many timecodes map to one second (`timeCodesPerSecond`). When the current time falls between two samples, USD *interpolates* the in-between value — linearly for most numeric types, or using the attribute’s declared interpolation mode for others.

##### Primvar

A primvar (short for *primitive variable*) is an attribute designed to carry data that varies across a geometric surface. Colors, texture coordinates (UV sets), and normals are typically primvars. Primvars have an *interpolation mode* that controls how values are distributed across geometry — for example, one value per vertex, or one value per face.

##### Purpose

Purpose is an attribute on imageable prims that lets renderers selectively show or hide groups of geometry without changing the scene structure. The built-in values are `default`, `render`, `proxy`, and `guide`. Use purpose to include high-resolution geometry for offline rendering, lighter proxies for interactive preview, and guide shapes visible only during authoring.

##### Active and Inactive Prims

Marking a prim *inactive* is USD’s way of non-destructively removing it. USD excludes an inactive prim and all its descendants from the stage, but the data stays in the layer and can be restored at any time. This is preferable to deleting prims when you want to preserve data or allow a downstream layer to override the state.

#### Assets and Organization

##### Asset and Asset Resolution

In USD, an *asset* is a reference to an external file, identified by a path string like `./textures/color.png`. *Asset resolution* turns that string into an actual file location.

##### Instancing

Instancing lets you place the same prim or asset multiple times in a scene while storing the data only once. All instances share a single copy of the geometry and materials, reducing file size and memory usage. Mark a prim as *instanceable* to enable this behavior. Instancing is well-suited to repeated objects like trees, crowd characters, or modular building pieces.

##### Kind and Model Hierarchy

Kind is metadata that classifies a prim’s role in the scene hierarchy. The built-in kinds are:

- **component** — a leaf asset such as a single prop or character.
- **group** — a prim that organizes other model prims without defining content itself.
- **assembly** — a group that combines multiple components into a larger asset or environment.

Tools use kind to navigate large scenes efficiently, focusing only on the prims relevant to a given task.

#### Rendering

##### Hydra

Hydra is USD’s rendering architecture. It separates *scene delegates* (which read scene data) from *render delegates* (which send data to a renderer), allowing you to swap renderers without changing how the scene delegate accesses data. On Apple platforms, Storm and the Raytracer are both Hydra-based renderers.

## Topics

### Related articles
- [Creating USD files for Apple devices](creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [Validating feature support for USD files](validating-usd-files.md)
  Ensure that the renderer that displays your USD assets supports its features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/usd-concepts)*