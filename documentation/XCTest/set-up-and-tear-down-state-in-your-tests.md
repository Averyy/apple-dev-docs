# Set Up and Tear Down State in Your Tests

**Framework**: Xctest

Prepare initial state before tests run, and clean up resources after tests complete.

#### Overview

To consistently and reliably check that your code produces the correct results, tests need to start from a known, predictable state. In some cases, you need to set up state once for all the test methods in a test class; in others, you need to reset to a known state before each test method.

After each test method or test class completes, you might want to delete files that you don’t need, such as temporary files or screenshots. Or, to assist in failure diagnosis, you might want to capture the final state after a test.

Prepare your known state for tests, and clean up temporary files after tests using the methods on [`XCTest`](xctest.md) and [`XCTestCase`](xctestcase.md).

##### Decide When to Set Up and Tear Down State in Your Test Class

When you run a test case, XCTest calls the `XCTestCase` `setUp()` class method first. Use this method to set up state common to all the test methods in your test class.

XCTest then runs each test method, calling setup and teardown methods in this order:

1. XCTest runs the setup methods once before each test method starts: `setUp() async throws` first, then `setUpWithError()`, then `setUp()`. Use these methods to prepare state that you need for each test method.
2. XCTest runs the test method.
3. XCTest runs the teardown blocks that you added in the test method, in last-in, first-out order. Use these blocks to tear down state and clean up resources after a specific test method.
4. XCTest runs the teardown methods once after each test method completes, with `tearDown()` first, then `tearDownWithError()`, then `tearDown() async throws`. Use these methods to tear down state after each test method.

When XCTest finishes running all the test methods and the test class completes, XCTest calls the `XCTestCase` `tearDown()` class method. Use this method to tear down state that’s common to all the test methods in your test class.

> 💡 **Tip**:  You can include test assertions in a test class’s `setUp() async throws`, `setUp()`, `setUpWithError()`, `tearDown() async throws`, `tearDown()`, and `tearDownWithError()` instance methods. XCTest evaluates these assertions as part of every test method’s run. However, you can’t include test assertions in a test class’s `setUp()` or `tearDown()` class methods. Test assertions require a test class instance, which doesn’t exist within the scope of class methods.

 You can include test assertions in a test class’s `setUp() async throws`, `setUp()`, `setUpWithError()`, `tearDown() async throws`, `tearDown()`, and `tearDownWithError()` instance methods. XCTest evaluates these assertions as part of every test method’s run. However, you can’t include test assertions in a test class’s `setUp()` or `tearDown()` class methods. Test assertions require a test class instance, which doesn’t exist within the scope of class methods.

##### Prepare and Tear Down State for a Test Class

For state that’s common to all the test methods in your test class and that doesn’t need a reset for each test method, use the [`setUp()`](xctestcase/setup().md) class method on [`XCTestCase`](xctestcase.md).

XCTest runs `setUp()` once before the test class begins.

If you need to clean up temporary files or capture any data that you want to analyze after the test class is complete, use the [`tearDown()`](xctestcase/teardown().md) class method on `XCTestCase`.

##### Prepare and Tear Down State for Each Test Method

For state that you need in each test method, choose one setup method from [`XCTest`](xctest.md) that fits best with your setup requirements:

- If your setup needs to prepare any state asynchronously, override [`setUp(completion:)`](xctest/setup(completion:).md).
- If your setup prepares all state synchronously and might throw errors, override [`setUpWithError()`](xctest/setupwitherror().md). This method catches thrown errors and records them as test failures.
- For tests that prepare state synchronously and don’t need to handle errors, override [`setUp()`](xctest/setup().md).

XCTest runs the setup methods once before each test method starts: `setUp() async throws` first, then `setUpWithError()`, then `setUp()`.

If you need to clean up temporary files or capture any data that you want to analyze after each test method is complete, override a teardown method from `XCTest`:

XCTest runs the teardown methods once after each test method completes: first `tearDown()`, then `tearDownWithError()`, then `tearDown() async throws`. Avoid preparing state for subsequent tests in the teardown methods. XCTest doesn’t guarantee that it will call teardown methods; if the test crashes before completion, XCTest doesn’t call the teardown blocks or methods.

> ❗ **Important**:  If your setup or teardown code needs to run on the Main actor, specify `@MainActor` for any asynchronous Swift setup or teardown methods you define. If you don’t specify an actor, the test executes asynchronous code in `setUp() async throws` and `tearDown() async throws` on an arbitrary actor.

 If your setup or teardown code needs to run on the Main actor, specify `@MainActor` for any asynchronous Swift setup or teardown methods you define. If you don’t specify an actor, the test executes asynchronous code in `setUp() async throws` and `tearDown() async throws` on an arbitrary actor.

##### Tear Down State After a Specific Test Method

For teardown that you need to complete immediately after a specific test method is complete, add a teardown block to the test method.

Your teardown block can call asynchronous Swift code using `await`, and you can throw errors that the test records as test failures.

If you register any teardown blocks during a test method’s execution, XCTest runs them after that test method ends but before XCTest calls the teardown instance method. XCTest runs teardown blocks on a last-in, first-out basis. XCTest calls registered teardown blocks and methods regardless of whether a test method passes or fails, even if you set the test case’s `continueAfterFailure` property to `false`.

Avoid preparing state for subsequent tests in teardown blocks. XCTest doesn’t guarantee that it will call teardown blocks; if the test crashes before completion, XCTest doesn’t call the teardown blocks.

> ❗ **Important**:  If any asynchronous Swift code you define in your teardown block needs to run on the Main actor, mark your teardown block `@MainActor`. If you don’t specify an actor, the test executes asynchronous code in teardown blocks on an arbitrary actor. If you call a throwing method with `try` in a teardown block, the block runs asynchronously.

 If any asynchronous Swift code you define in your teardown block needs to run on the Main actor, mark your teardown block `@MainActor`. If you don’t specify an actor, the test executes asynchronous code in teardown blocks on an arbitrary actor. If you call a throwing method with `try` in a teardown block, the block runs asynchronously.

## See Also

- [class func setUp()](xctestcase/setup.md)
  Provides an opportunity to customize initial state before a test case begins.
- [func addTeardownBlock(() async throws -> Void)](xctestcase/addteardownblock(_:)-2guon.md)
  Registers a block of teardown code to run after the current test method ends.
- [func addTeardownBlock(() throws -> Void)](xctestcase/addteardownblock(_:)-5zw6c.md)
  Registers a block of teardown code to run after the current test method ends.
- [class func tearDown()](xctestcase/teardown.md)
  Provides an opportunity to perform cleanup after a test case ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/set-up-and-tear-down-state-in-your-tests)*