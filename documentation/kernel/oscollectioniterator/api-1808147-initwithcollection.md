# initWithCollection

**Framework**: Kernel  
**Kind**: instm

Initializes an OSCollectionIterator for the provided collection object.

## Declaration

```swift
virtual bool initWithCollection(
 const OSCollection *inColl);
```

#### Return_value

`true` if the initialization was successful, or `false` on failure.

#### Overview

Not for general use. Use the static instance creation method withCollection instead.

## Parameters

- `inColl`: The OSCollection-derived collection object to be iteratated.

## See Also

- [free](oscollectioniterator/1808113-free.md)
  Releases or deallocates any resources used by the OSCollectionIterator object.
- [getNextObject](oscollectioniterator/1808125-getnextobject.md)
  Advances to and returns the next object in the iteration.
- [isValid](oscollectioniterator/1808157-isvalid.md)
  Checks that the collection hasn't been modified during iteration.
- [reset](oscollectioniterator/1808170-reset.md)
  Resets the iterator to the beginning of the collection, as if it had just been created.
- [withCollection](oscollectioniterator/1808183-withcollection.md)
  Creates and initializes an OSCollectionIterator for the provided collection object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollectioniterator/1808147-initwithcollection)*