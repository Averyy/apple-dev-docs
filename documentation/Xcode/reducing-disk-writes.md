# Reducing disk writes

**Framework**: Xcode

Improve your app’s responsiveness by optimizing how it writes data to permanent storage.

#### Overview

All iOS devices and some macOS devices use a solid-state drive (SSD) for permanent storage. Accessing your data on SSD, or any long-term storage media, is slow compared to RAM. In addition, the system can only write to the same region of SSD a limited number of times before that region wears out.

Use Xcode and Instruments to understand your app’s disk-writing performance, including the total amount of data written, the size of writes, excessive storage write exceptions, and other possible optimizations.

##### Optimize Ssd Access

When the system writes to a block on the SSD, new read requests for that block are queued until the write operation completes. Writing to an SSD is a slower operation than reading. Interleaving read and write requests can slow your app’s performance.

Optimize your app’s performance by reducing the number of write operations to an SSD. For example, create temporary files in a cache in the RAM whenever possible.

##### Eliminate Excessive Write Operations

The system throws an exception and generates a report when the disk writes from your app exceed a certain threshold in a 24-hour period. View the aggregated exception logs for a version of your app in the Disk Writes pane in Xcode Organizer or capture them with [`MetricKit`](https://developer.apple.com/documentation/MetricKit).

![Labeled screenshot of the Disk Write reports pane in the Xcode Organizer. From left to](https://docs-assets.developer.apple.com/published/eea210b4300d4494095db4fbcac971ce/reducing-disk-writes-1%402x.png)

Each report in the Report List shows the function call that generated the exception and the percentage of total disk writes it accounted for. Clicking on a report shows a sample stack trace, as well as additional details in the Inspector, including:

- iOS software version
- Device model
- Total writes
- Number of logs received
- 14-day reporting trend

Prioritize fixing exceptions by using the total percentage of disk writes, as well as information on the operating system and the impacted device types. Identify the code that’s causing the increase in writes by using the function signature for a specific report in the Report List and the corresponding stack trace. After updating the code and verifying the fix, mark the report as resolved.

##### Gather Metrics About Your Apps Disk Usage

View the daily amount of data your app writes to the disk in the Disk Writes metrics pane of the Xcode Organizer window or by using [`MetricKit`](https://developer.apple.com/documentation/MetricKit).

The pane displays the logical disk writes in megabytes per day for the shipping versions of your app. Compare versions to find unexpected increases. Filter to find differences between devices and to view the typical amount of data written (50th percentile) or the largest amount (90th percentile). MetricKit reports the same data.

The screenshot below shows that the largest amount of data written by the latest version of the MealPlanner app is 24.4 MB more per day than an earlier version.

![Screenshot of the Disk Writes metric pane in the Xcode Organizer. From left to right is](https://docs-assets.developer.apple.com/published/64118eb84a67b2c2f5daa1b5c4b5dcfa/reducing-disk-writes-2%402x.png)

Assess whether the amount of data recorded seems reasonable for your app. If the numbers are greater than what you expect, you may be writing data too frequently. For example, if your app’s files total 100 KB and your app writes 500 MB of data to disk every day, you might want to investigate how many times you’re writing the same data to disk each day.

Use the graph of disk-write frequency by versions to identify trends in disk usage. An app whose writes increase daily might either be legitimately handling more data or inefficiently handling existing data. Spikes might indicate either the user created or downloaded new content for your app, or your app modified the same content even more than usual. Dips might help you identify the smallest subset of data required by your app.

##### Identify the Code Causing Significant Disk Writes

Profile your app in Instruments, using the File Activity template. Instruments tracks the logical and physical use of storage by your app.

![Illustration showing the logical and physical disk usage timelines in](https://docs-assets.developer.apple.com/published/b819a954ec07ed55ea5d4440b31f1ed2/reducing-disk-writes-3.png)

The Filesystem Activity instrument records logical filesystem use in the form of system calls to read or write data, or to map filesystem data into memory. Instruments associates each event with its size, duration, and a backtrace you can use to identify the code that’s using the filesystem. The Disk Usage and Disk I/O Latency instruments report the physical use of the storage medium resulting from the filesystem events by showing the size and latency of reads and writes.

The Filesystem Suggestions instrument and the Disk Writes Reports pane in the Xcode Organizer also offer suggestions for addressing common filesystem use issues.

> **Note**: The size of physical reads and writes on the disk doesn’t correlate with the size of logical filesystem activity. The disk controller works with regions called blocks, frequently 4 KB in size. Writes to the disk occur in units of blocks, so saving a file with only a single-byte change writes 4 KB to the disk.

##### Batch Multiple Write Operations

Repeatedly opening, saving, and then closing the same file can increase the frequency of disk writes. Collecting small changes and performing them as a single write reduces the frequency, though it can also result in an increase in your app’s memory use. Design your app’s persistence model to effectively balance its use of these two resources. See [`Reducing your app’s memory use`](reducing-your-app-s-memory-use.md).

##### Minimize Writing to Serialized Files

Many apps use property list, JSON, XML, or other serialized formats for writing user documents. These formats are good for read-only content, such as bundle metadata, or to transfer data over the network. The formats aren’t optimal to store user documents that frequently change. Changing a serialized document requires rewriting the entire file, which increases the latency of the operation and the wear on the device.

When possible, use Core Data or SQLite for storing frequently edited documents. If that isn’t possible, use different serialized files for data that changes frequently and data that’s mostly static. This can reduce the amount of disk writes and improve latency.

The Disk Writes Report pane offers suggestions for optimizing the use of serialized files.

##### Avoid Rapid File Creation and Deletion

When you create or delete a file on iOS, the system updates the directory reference by writing 8 KB of metadata. Rapidly creating or deleting lots of files results in many small writes to the filesystem, degrading performance and increasing wear on the device. Renaming or moving a file on iOS adds up to 16 KB in filesystem metadata writes.

Creating a file atomically adds additional writes because the system must create a temporary file, write the content, unlink an existing destination file, then rename the temporary file to the final destination. Common use cases include the atomic write calls for Foundation objects, such as [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), and [`NSData`](https://developer.apple.com/documentation/Foundation/NSData).

Use atomic writes only when needed.

##### Minimize Explicit Storage Synchronization

Writing data on iOS adds the data to a unified buffer cache that the system then writes to file storage. Forcing iOS to flush pending filesystem changes from the unified buffer can result in unnecessary writes to the disk, degrading performance and increasing wear on the device. When possible, avoid calling `fsync(_:)`, or using the `fcntl(_:_:)` `F_FULLFSYNC` operation to force a flush.

Some apps require a  to ensure data persistence before subsequent operations can proceed. Most apps can use the `fcntl(_:_:)` `F_BARRIERFSYNC` for this.

Only use `F_FULLFSYNC` when your app requires a strong expectation of data persistence. Note that `F_FULLFSYNC` represents a best-effort guarantee that iOS writes data to the disk, but data can still be lost in the case of sudden power loss.

##### Prevent Regressions in Disk Write Frequency

Measure the disk usage of your app by writing an XCTest performance test. Create a test that passes an instance of [`XCTStorageMetric`](https://developer.apple.com/documentation/XCTest/XCTStorageMetric) to the [`measure(metrics:block:)`](https://developer.apple.com/documentation/XCTest/XCTestCase/measure(metrics:block:)) function. Call your code inside the block argument of `measure(metrics:block:)`, the method that writes data to disk.

The test measures the number of blocks written to the filesystem to save your data. Set a baseline expectation for the amount of disk use. The test fails if the amount of data written significantly exceeds the baseline.

```swift
func testDiskUse() {
  self.measure(metrics: [XCTStorageMetric()]) {
     // This is a disk-intensive operation.
  }
}
```

##### Use Core Data or Sqlite Databases for Frequently Changing Documents

SQLite is highly optimized for efficient access to storage. It uses in-memory caches and batched disk-writes to ensure high performance and minimal wear on storage. The data structures are designed to allow efficient updates when inserting new content or updating existing content.

Core Data takes advantage of SQLite’s efficient disk usage for storing your data. Core Data also uses the SQLite best practices described below.

###### Avoid Unnecessarily Closing Sqlite Connections

Opening and closing SQLite connections are expensive operations that require SQLite to write out all pending changes, along with additional metadata including consistency checks and journaling logs. Take better advantage of SQLite’s efficiency by closing a connection only when there’s a clear need.

###### Use Transactions

Use transactions to perform a consolidated write operation for related changes, such as editing multiple fields in a single document. Each transaction can contain multiple `INSERT`, `UPDATE`, and `DELETE` statements.

Transactions are also atomic. Either all of the changes are saved to the database, or the database is restored to the state prior to the transaction. This prevents the database from being left in an inconsistent state.

###### Use Appropriate Indices

Decrease search time and avoid unnecessary writes to the disk by using appropriate indices on your database tables. For example, an email app that uses SQLite may show all inbox messages in chronological order using the following SQL statement:

```None
SELECT * FROM messages WHERE folder LIKE ‘Inbox’ ORDER BY sent_time
```

Without an index on the `sent_time` column, SQLite constructs a temporary B-tree in memory, reads the whole table, and performs the sort using the B-tree. If the data in the B-tree is too large for the in-memory cache, SQLite writes it to the disk, further slowing the query. With an index on `sent_time`, SQLite reads the messages in order and returns matching rows.

Use a partial index for columns representing information that doesn’t require searching each of the rows, such as rows that can contain `NULL`. A partial index — one with a `WHERE` clause — provides a performance advantage while taking up less disk space than a full index.

Use `EXPLAIN QUERY PLAN` to determine if a query can benefit from optimization. The following code shows the explanation of a query on an unindexed `sent_time` column.

```None
> EXPLAIN QUERY PLAN SELECT * FROM messages WHERE folder
  LIKE ‘Inbox’ ORDER BY sent_time

QUERY PLAN
|--SEARCH TABLE <>
|--SEARCH TABLE <>
--*USE TEMP B-TREE FOR ORDER BY*
```

The presence of `USE TEMP B-TREE FOR ORDER BY` in the output indicates that the query requires a temporary B-tree to sort the results.

The Disk Writes Report pane suggestions identify queries that may benefit from an index.

###### Use Write Ahead Logging Journaling Mode

Enable more efficient reads and writes in SQLite by using write-ahead logging (WAL) journaling mode. This mode enables coalescing multiple writes to the same page, reducing SQLite’s use of write barriers, and supporting multiple database read threads in parallel with a writer.

Use `PRAGMA journal_mode` to determine your SQLite database’s journaling mode. Use `PRAGMA journal_mode=WAL` to change to write-ahead logging mode.

The Disk Writes Report pane suggests using write-ahead logging when a stack trace indicates a different journaling mode.

###### Avoid Using the Explicit Vacuum Command

Using the SQLite `VACUUM` command saves space by rebuilding the database. The operation copies the existing database to a temporary file, then moves information back into the database, which may result in excessive disk writes.

When possible, rebuild the database incrementally by setting the `auto_vacuum()` pragma to `2`. Then use the `incremental_vacuum()` pragma to remove any existing empty pages from the free pages list.

The Disk Writes Report pane suggests using incremental vacuuming when a stack trace indicates the database is in full auto-vacuum mode.

## See Also

- [Analyzing responsiveness issues in your shipping app](analyzing-responsiveness-issues-in-your-shipping-app.md)
  Identify responsiveness issues your users encounter, and use the hang and hitch data in Xcode Organizer to determine which issues are most important to fix.
- [Improving app responsiveness](improving-app-responsiveness.md)
  Create a user experience that feels responsive by removing hangs and hitches from your app.
- [Understanding user interface responsiveness](understanding-user-interface-responsiveness.md)
  Make your app more responsive by examining the event-handling and rendering loop.
- [Understanding and improving SwiftUI performance](understanding-and-improving-swiftui-performance.md)
  Identify and address long-running view updates, and reduce the frequency of updates.
- [Understanding hangs in your app](understanding-hangs-in-your-app.md)
  Determine the cause for delays in user interactions by examining the main thread and the main run loop.
- [Understanding hitches in your app](understanding-hitches-in-your-app.md)
  Determine the cause of interruptions in motion by examining the render loop.
- [Diagnosing performance issues early](diagnosing-performance-issues-early.md)
  Diagnose potential performance issues in your app during testing with the Thread Performance Checker tool in Xcode.
- [Reducing your app’s launch time](reducing-your-app-s-launch-time.md)
  Create a more responsive experience with your app by minimizing time spent in startup.
- [Reducing terminations in your app](reduce-terminations-in-your-app.md)
  Minimize how frequently the system stops your app by addressing common termination reasons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reducing-disk-writes)*