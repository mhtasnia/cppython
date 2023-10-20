gdp_1, gdp_2 = map(float, input().split())
whole_gdp = ((1+(gdp_1/100))*(1+(gdp_2/100)))-1
print("%0.6f" % (whole_gdp*100))
