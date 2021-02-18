df_handles_count <- read_csv("~/Google Drive/diss_detection/df_handles_count.csv")

df_handles_count$republican <- ifelse(df_handles_count$party=="R", 1, 0)
df_handles_count$female <- ifelse(df_handles_count$gender=="F", 1, 0)

hist(df_handles_count$followers_count, breaks = 100)
df_handles_count$followers_count_log <- log(df_handles_count$followers_count+1)
hist(df_handles_count$statuses_count, breaks = 100)
df_handles_count$statuses_count_log <- log(df_handles_count$statuses_count+1)

df_handles_count$office <- as.factor(df_handles_count$office)
df_handles_count$office <- relevel(df_handles_count$office, ref="representative")
df_handles_count_subset <- df_handles_count[which(df_handles_count$handle != "@realDonaldTrump" 
                                               & df_handles_count$office!= "collective" ),]

h_office <- glm(handle_include_count ~ office, data = df_handles_count_subset,  family = poisson)
h_female <- glm(handle_include_count ~ female, data = df_handles_count_subset,  family = poisson)
h_republican <- glm(handle_include_count ~ republican, data = df_handles_count_subset,  family = poisson)
h_follower <- glm(handle_include_count ~ followers_count_log, data = df_handles_count_subset,  family = poisson)
h_status <- glm(handle_include_count ~ statuses_count_log, data = df_handles_count_subset,  family = poisson)
h_all <- glm(handle_include_count ~ office + female + republican + followers_count_log + statuses_count_log, data = df_handles_count_subset,  family = poisson)
texreg(list(h_office, h_female, h_republican, h_follower, h_status, h_all))

m_office <- glm(mention_count ~ office, data = df_handles_count_subset,  family = poisson)
m_female <- glm(mention_count ~ female, data = df_handles_count_subset,  family = poisson)
m_republican <- glm(mention_count ~ republican, data = df_handles_count_subset,  family = poisson)
m_follower <- glm(mention_count ~ followers_count_log, data = df_handles_count_subset,  family = poisson)
m_status <- glm(mention_count ~ statuses_count_log, data = df_handles_count_subset,  family = poisson)
m_all <- glm(mention_count ~ office + female + republican + followers_count_log + statuses_count_log, data = df_handles_count_subset,  family = poisson)
texreg(list(m_office, m_female, m_republican, m_follower, m_status, m_all))

df_handles_count_subset_congress <- df_handles_count[which(df_handles_count$handle != "@realDonaldTrump" 
                                                  & (df_handles_count$office == "representative" |  
                                                       df_handles_count$office == "senator")),]
summary(glm(handle_include_count ~ republican + female + followers_count_log + statuses_count_log, data = df_handles_count_subset_congress,  family = poisson))
summary(glm(handle_include_count ~ office*republican + female + followers_count_log + statuses_count_log, data = df_handles_count_subset_congress,  family = poisson))

