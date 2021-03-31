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

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

nvm install 14.15
nvm use node
node -v

npm install -g eslint@7.0.0 stylelint@13.3.3 eslint-plugin-vue@latest
npm install

run_test "eslint --ext .js,.vue ${DJANGO_APP}/static/${DJANGO_APP}/js/components/"
run_test "eslint --ext .js,.vue ${DJANGO_APP}/static/${DJANGO_APP}/js/pages/"
run_test "stylelint '${DJANGO_APP}/**/*.vue' '${DJANGO_APP}/**/*.css' '${DJANGO_APP}/**/*.scss'"

run_test "coverage run --source=${DJANGO_APP} '--omit=*/migrations/*' manage.py test ${DJANGO_APP}"

# put generaged coverage result where it will get processed
cp .coverage.* /coverage

exit 0
