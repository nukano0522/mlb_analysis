library(dplyr)
library(purrr)
library(stringr)

data2016 <- read.csv(
  "C:/Users/nukan/Documents/MLB_analysis/data/data2016.csv", 
  sep='\t',
  colClasses = c('character', 'character', 'character', 'numeric')
)

T_matrix <- data2016 %>%
  select(state, new.state) %>%
  table()

P_matrix <- prop.table(T_matrix, 1)

count_runners_out <- function(s) {
  s %>%
    str_split("") %>%
    pluck(1) %>%
    as.numeric() %>%
    sum(na.rm = TRUE)
}

runners_out <- sapply(row.names(T_matrix), 
                      count_runners_out)[-25]

R <- outer(runners_out + 1, runners_out, FUN = "-")
names(R) <- names(T_matrix)[-25]
R <- cbind(R, rep(0,24))
