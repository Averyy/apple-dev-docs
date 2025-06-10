# getNextObject

**Framework**: Kernel  
**Kind**: instm

Advances to and returns the next object in the iteration.

## Declaration

```swift
virtual OSObject * getNextObject();
```

#### Return_value

The next object in the iteration context, `NULL` if there is no next object or if the iterator is no longer valid.

#### Overview

This function first calls isValid and returns `NULL` if that function returns `false`.

Subclasses must implement this pure virtual function to check for validity with isValid, and then to advance the iteration context to the next object (if any) and return that next object, or `NULL` if there is none.

## See Also

- [free](oscollectioniterator/1808113-free.md)
  Releases or deallocates any resources used by the OSCollectionIterator object.
- [initWithCollection](oscollectioniterator/1808147-initwithcollection.md)
  Initializes an OSCollectionIterator for the provided collection object.
- [isValid](oscollectioniterator/1808157-isvalid.md)
  Checks that the collection hasn't been modified during iteration.
- [reset](oscollectioniterator/1808170-reset.md)
  Resets the iterator to the beginning of the collection, as if it had just been created.
- [withCollection](oscollectioniterator/1808183-withcollection.md)
  Creates and initializes an OSCollectionIterator for the provided collection object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollectioniterator/1808125-getnextobject)*