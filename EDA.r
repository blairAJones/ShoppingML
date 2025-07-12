library(ggplot2)
library(tidyverse)

iphones = read.csv("iphone_cleaned.csv")
head(iphones)

ggplot(iphones) +
  geom_histogram(price.value)