#! /bin/bash
DATE=`date | sed 's/ /_/g' | sed 's/:/_/g'`
PRODUCT_NAME="PRODUCT_"
PRODUCT_FULL_NAME=${PRODUCT_NAME}${DATE}".tar"


tar -cf ${PRODUCT_FULL_NAME} source/product.py install.sh execute.sh
echo ${PRODUCT_FULL_NAME}
