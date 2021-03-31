trap 'exit 1' ERR

#
# PRECONDITION: inherited env vars MUST include:
#      DJANGO_APP: django application directory name

# start virtualenv
source bin/activate

function run_test {
    echo "##########################"
    echo "TEST: $1"
    eval $1
}

run_test "pycodestyle ${DJANGO_APP}/ --exclude=migrations,static"

run_test "eslint --ext .js,.vue ${DJANGO_APP}/static/${DJANGO_APP}/js/components/"
run_test "eslint --ext .js,.vue ${DJANGO_APP}/static/${DJANGO_APP}/js/pages/"
run_test "stylelint '${DJANGO_APP}/**/*.vue' '${DJANGO_APP}/**/*.css' '${DJANGO_APP}/**/*.scss'"

run_test "coverage run --source=${DJANGO_APP} '--omit=*/migrations/*' manage.py test ${DJANGO_APP}"

# put generaged coverage result where it will get processed
cp .coverage.* /coverage

exit 0
