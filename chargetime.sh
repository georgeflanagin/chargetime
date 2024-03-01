function chargetime
{
    command pushd ~/chargetime > /dev/null
    python chargetime.py $@
    command popd > /dev/null

}
