# objectRestorationClass

**Framework**: UIKit  
**Kind**: property

The class responsible for creating this object when restoring the app’s state.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional var objectRestorationClass: (any UIObjectRestoration.Type)? { get }
```

#### Discussion

If an object has an associated restoration class, the [`object(withRestorationIdentifierPath:coder:)`](uiobjectrestoration/object(withrestorationidentifierpath:coder:).md) method of that class is called during state restoration. That method is responsible for returning the object that matches the provided path identifier information. If this property is`nil`, the object must already exist and be registered with the state restoration engine so that it can be found implicitly. You can register the object using the [`registerObject(forStateRestoration:restorationIdentifier:)`](uiapplication/registerobject(forstaterestoration:restorationidentifier:).md) method at launch time.

The restoration class must conform to the [`UIObjectRestoration`](uiobjectrestoration.md) protocol.

## See Also

- [var restorationParent: (any UIStateRestoring)?](uistaterestoring/restorationparent.md)
  The parent object used to scope the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistaterestoring/objectrestorationclass)*