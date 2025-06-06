# MetalPerformanceShaders Functions

**Framework**: Metal Performance Shaders

## Topics

### Functions
- [func MPSDataTypeBitsCount(MPSDataType) -> Int](4316495-mpsdatatypebitscount.md)
- [func MPSFindIntegerDivisionParams(UInt16) -> MPSIntegerDivisionParams](2954868-mpsfindintegerdivisionparams.md)
  Returns the integer division parameters for a specified divisor. 
- [func MPSGetCustomKernelBatchedDestinationIndex(MPSCustomKernelArgumentCount) -> UInt](2990481-mpsgetcustomkernelbatcheddestina.md)
  Returns the index of the first destination texture argument.
- [func MPSGetCustomKernelBatchedSourceIndex(MPSCustomKernelArgumentCount, UInt, UInt) -> UInt](2990482-mpsgetcustomkernelbatchedsourcei.md)
  Returns the index of the specified batched source texture argument.
- [func MPSGetCustomKernelBroadcastSourceIndex(MPSCustomKernelArgumentCount, UInt, UInt) -> UInt](2990483-mpsgetcustomkernelbroadcastsourc.md)
  Returns the index of the specified nonbatched source texture argument.
- [func MPSGetCustomKernelMaxBatchSize(MPSCustomKernelArgumentCount, UInt) -> UInt](2990484-mpsgetcustomkernelmaxbatchsize.md)
  Returns the maximum allowed batch size.
- [func MPSGetImageType(MPSImage) -> MPSImageType](3131717-mpsgetimagetype.md)
- [func MPSGetPreferredDevice(MPSDeviceOptions) -> (any MTLDevice)?](3088918-mpsgetpreferreddevice.md)
- [func MPSHintTemporaryMemoryHighWaterMark(any MTLCommandBuffer, Int)](2990485-mpshinttemporarymemoryhighwaterm.md)
  Triggers Metal Performance Shaders to prefetch a Metal heap of the indicated size into its internal cache.
- [func MPSImageBatchIncrementReadCount([MPSImage], Int) -> Int](2951916-mpsimagebatchincrementreadcount.md)
  Increments or decrements the read count of an image batch by a specified amount.
- [func MPSImageBatchIterate([MPSImage], (MPSImage, Int) -> Int) -> Int](3019319-mpsimagebatchiterate.md)
  Executes a callback block once for each unique image in a batch.
- [func MPSImageBatchResourceSize([MPSImage]) -> Int](2980727-mpsimagebatchresourcesize.md)
  Returns the number of bytes used to allocate the specified image batch.
- [func MPSImageBatchSynchronize([MPSImage], any MTLCommandBuffer)](2953951-mpsimagebatchsynchronize.md)
  Removes any copy of the specified image batch from the device's caches, and, if needed, invalidates any CPU caches.
- [func MPSSetHeapCacheDuration(any MTLCommandBuffer, Double)](2990486-mpssetheapcacheduration.md)
  Sets the timeout after which unused cached Metal heaps are released.
- [func MPSSizeofMPSDataType(MPSDataType) -> Int](4092019-mpssizeofmpsdatatype.md)
- [func MPSStateBatchIncrementReadCount([MPSState]?, Int) -> Int](2951920-mpsstatebatchincrementreadcount.md)
  Increments or decrements the read count of a state batch by a specified amount.
- [func MPSStateBatchResourceSize([MPSState]?) -> Int](2980728-mpsstatebatchresourcesize.md)
  Returns the number of bytes used to allocate the specified state batch.
- [func MPSStateBatchSynchronize([MPSState], any MTLCommandBuffer)](2953920-mpsstatebatchsynchronize.md)
  Removes any copy of the specified state batch from the device's caches, and, if needed, invalidates any CPU caches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/metalperformanceshaders_functions)*