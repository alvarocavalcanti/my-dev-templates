# QA Strategy

## Description

Here you can find information regarding our QA Strategy, specifying the goals we want to achieve and the reasoning behind them.

## Scenario

Here we have the full scenario, considering two **environments**, `LOCAL` and `CI`. Also, note that the `COMMIT` and `PUSH` stages rely on [git hooks](https://git-scm.com/book/gr/v2/Customizing-Git-Git-Hooks), `pre-commit` and `pre-push` respectively, being properly setup on `LOCAL` environments.

### `COMMIT`

`LOCAL`:

- Lint

`CI`:

- [None]

### `PUSH`

`LOCAL`:

- Unit Tests
- Integration Tests [<sup>1</sup>](#footnotes)
- Test Coverage

`CI`:

- Unit Tests
- Integration Tests
- Test Coverage
- UI Tests [<sup>2</sup>](#footnotes)

### `BUILD/RELEASE`

`LOCAL`:

- [None]

`CI`:

- Integration Tests
- UI Tests

### `DEPLOY`

`LOCAL`:

- [None]

`CI`:

- Smoke Tests
- Regression/E2E Tests

## Terms Description

### Behold The Pyramid

Before anything, be aware of the [test pyramid](https://martinfowler.com/bliki/TestPyramid.html):

![Test Pyramid](https://martinfowler.com/bliki/images/testPyramid/test-pyramid.png)

Simply put, test at the top are more expensive and slower, while tests at the bottom a cheaper and faster. Ww should have much more Unit tests as opposed to UI tests.

### Lint

Static code analysis. Checks for things like unused imports, formatting issues and even cyclomatic complexity.

It's entirely up to us to decide the best configuration, being able to start small and improve it as time goes by.

### Unit

Unit tests should test only the behaviour of the subject in question, and only the code we have written (not the libraries we use).

Here we can use mocks to isolate this behaviour. An insightful post on the matter: [Mocks aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html).

Even though they're largely easier to spot on the backend, there should also be frontend unit tests. We should have them all.

### Integration/Service

An integration test is a test that goes from a little extra mile over unit tests until right before end-to-end testing.

Tests that touch the database, that checks information exchagen across services, etc.

### Test Coverage

An analysis of how much of the codebase is covered by tests. The results are in percentage and we should decide on a threshold for failing the build.

It's completely alright to start with a really low bar and people agree, in general, that having something between 60-80% is a good coverage.

### UI

Testing the UI involves interacting directly with the UI in an automated manner.

Be mindful that UI tests aren't, necesserally end-to-end tests. They might be executed within a single screen context with provided data, and make assertions on the UI's behaviour, thus Unit UI Tests.

### Smoke

Does smoke come out of it when you turn it on? That's the idea here. After doing a deploy (be it to staging or production) we should run a really quick, yet informative test.

A good start is doing several pings, to all the frontends, the backend and the services we consume.

### Regression/E2E

A regression suite is a set of tests that represent the most important features, which whould never be broken.

These tests should be end-to-end, meaning that there aren't any kind of mocking or dummy data. They should rely on the availability of the external services.

Sometimes it's ok to mock specific dependencies to improve speed for specific group of tests.

#### Footnotes

1. If the integration test suite gets too big/slow it can be skipped at this stage

1. If ui test suite gets too big/slow it can be skipped at this stage