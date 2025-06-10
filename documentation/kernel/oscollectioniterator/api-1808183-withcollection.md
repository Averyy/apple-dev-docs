# withCollection

**Framework**: Kernel  
**Kind**: instm

Creates and initializes an OSCollectionIterator for the provided collection object.

## Declaration

```swift
static OSCollectionIterator * withCollection(
 const OSCollection *inColl);
```

#### Return_value

A new instance of OSCollectionIterator, or `NULL` on failure.

## Parameters

- `inColl`: The OSCollection-derived collection object to be iteratated.

## See Also

- [free](oscollectioniterator/1808113-free.md)
  Releases or deallocates any resources used by the OSCollectionIterator object.
- [getNextObject](oscollectioniterator/1808125-getnextobject.md)
  Advances to and returns the next object in the iteration.
- [initWithCollection](oscollectioniterator/1808147-initwithcollection.md)
  Initializes an OSCollectionIterator for the provided collection object.
- [isValid](oscollectioniterator/1808157-isvalid.md)
  Checks that the collection hasn't been modified during iteration.
- [reset](oscollectioniterator/1808170-reset.md)
  Resets the iterator to the beginning of the collection, as if it had just been created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollectioniterator/1808183-withcollection)*