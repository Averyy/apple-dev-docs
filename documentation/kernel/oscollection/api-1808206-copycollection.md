# copyCollection

**Framework**: Kernel  
**Kind**: instm

Creates a deep copy of a collection.

## Declaration

```swift
virtual OSCollection *copyCollection(
 OSDictionary *cycleDict = 0);
```

#### Return_value

The newly copied collecton, `NULL` on failure.

#### Overview

This function copies the collection and all of the contained collections recursively. Objects that are not derived from OSCollection are retained rather than copied.

Subclasses of OSCollection must override this function to properly support deep copies.

## Parameters

- `cycleDict`: A dictionary of all of the collections that have been copied so far, to start the copy at the top level pass   for  .

## See Also

- [ensureCapacity](oscollection/1808212-ensurecapacity.md)
  Ensures the collection has enough space to store the requested number of objects.
- [flushCollection](oscollection/1808219-flushcollection.md)
  Empties the collection, releasing any objects retained.
- [getCapacity](oscollection/1808225-getcapacity.md)
  Returns the number of objects the collection can store without reallocating.
- [getCapacityIncrement](oscollection/1808233-getcapacityincrement.md)
  Returns the storage increment of the collection.
- [getCount](oscollection/1808238-getcount.md)
  Returns the number of objects in the collection.
- [getNextObjectForIterator](oscollection/1808244-getnextobjectforiterator.md)
  Returns the next member of a collection.
- [haveUpdated](oscollection/1808248-haveupdated.md)
  Tracks updates to the collection.
- [init](oscollection/1808252-init.md)
  Initializes the OSCollection object.
- [initIterator](oscollection/1808258-inititerator.md)
  Initializes the iteration context for a collection subclass.
- [iteratorSize](oscollection/1808262-iteratorsize.md)
  Returns the size in bytes of a subclass's iteration context.
- [setCapacityIncrement](oscollection/1808267-setcapacityincrement.md)
  Sets the storage increment of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollection/1808206-copycollection)*