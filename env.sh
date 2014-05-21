
# source this to activate virtual environment

echo Checking for virtualenv
virtualenv --version > /dev/null|| pip install virtualenv


mkdir -p var/bin var/tmp var/log var/etc var/log/pawtrain
if [ ! -e var/bin/activate ]; then
    echo Creating virtual environment...
    virtualenv var > /dev/null
    echo done!
fi

echo Activating virtual environment...
. var/bin/activate

echo Installing any necessary libraries...

# For MacOS X 10.9, when buidling Pillow, the cc uses an invalid
# command line option; this forces XCode to ignore it (at least for now).
#
OS=`uname -s`
if [ "x$OS" = "xDarwin" ]; then
    echo Working around MacOS compiler weirdness...
    export ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future
fi

if [ -d /var/cache/drone ]; then
    export PIP_DOWNLOAD_CACHE=/var/cache/drone/pip-cache
else
    export PIP_DOWNLOAD_CACHE=/var/tmp/pip-cache
fi
mkdir -p $PIP_DOWNLOAD_CACHE && chmod a+t $PIP_DOWNLOAD_CACHE
pip install -r requirements.txt

echo done!


