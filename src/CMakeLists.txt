set(STOCK_LIB_SRC
	black_scholes.cpp
	black_scholes.h)

add_library(StockLib SHARED ${STOCK_LIB_SRC})
