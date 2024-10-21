install:
    /bin/bash run install_dependencies

test:
    /bin/bash run test:all

test-x:
    /bin/bash run test:stop-at-first-fail

test-lf:
    /bin/bash run test:last-fail

clean:
    /bin/bash run clean

lint:
    /bin/bash run lint

init_git_and_commit:
    /bin/bash run init_git_and_commit