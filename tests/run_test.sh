SAVED_MUP_ROOT=$MUP_ROOT
SAVED_MUP_DB=$MUP_DB
export MUP_ROOT=`mktemp -d`/
export MUP_DB=${MUP_ROOT}temp-mup-db

python test_meta_ultra.py

#export MUP_ROOT=$SAVED_MUP_ROOT
#export MUP_DB=$SAVED_MUP_DB
