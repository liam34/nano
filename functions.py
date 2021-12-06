risk = function(psa, age, race, priorbiopsy, dre, famhistory) {
  ##### create persons data set
  data=c(1, log(psa,2), age, race)
  # prior biopsy known?
  a = as.numeric(is.na(priorbiopsy)==FALSE)
  if(a==1){data=c(data, priorbiopsy)}
  # DRE was recorded?
  b = as.numeric(is.na(dre)==FALSE)
  if(b==1){data=c(data, dre)}
  # family history was recorded?
  c = as.numeric(is.na(famhistory)==FALSE)
  if(c==1){data=c(data, famhistory)}
  ##### choose correct model
  if(a==1 & b==1 & c==1){
    # PSA, age, race, priorbiopsy, DRE, familyhistory
    no.low=c(-3.00215469, 0.25613390, 0.01643637, 0.12172599, -0.45533257,
             -0.03864628, 0.27197219)
    no.high=c(-7.05304534, 0.70489441, 0.04753804, 1.04174529, -0.21409933,
              0.40068434, 0.22467348)
  }
  if(a==1 & b==1 & c==0){
    # PSA, age, race, priorbiopsy, DRE
    no.low=c(-2.89648245, 0.25904098, 0.01559192, 0.11996693, -0.45444000,
             -0.03729244)
    no.high=c(-6.96119633, 0.70674359, 0.04676393, 1.03937720, -0.21100921,
              0.40319606)
  }
  if(a==1 & b==0 & c==1){
    # PSA, age, race, priorbiopsy, familyhistory
    no.low=c(-3.01529063, 0.25578861, 0.01654912, 0.12327661, -0.45825158,
             0.27183869)
    no.high=c(-6.94522156, 0.70637260, 0.04697087, 1.02065099, -0.18320006,
              0.23044734)
  }
  if(a==1 & b==0 & c==0){
    # PSA, age, race, priorbiopsy
    no.low=c(-2.90917471, 0.25872451, 0.01570165, 0.12141077, -0.45729181)
    no.high=c(-6.85264083, 0.70797314, 0.04621214, 1.01887797, -0.17972927)
  }

  if(a==0 & b==1 & c==1){
    # PSA, age, race, DRE, familyhistory
    no.low=c(-2.90933651, 0.23803667, 0.01447269, 0.11443251, -0.06592322,
             0.27128248)
    no.high=c(-6.99449483, 0.69530025, 0.04637911, 1.03847001, 0.38651649,
              0.22287791)
  }
  if(a==0 & b==1 & c==0){
    # PSA, age, race, DRE
    no.low=c(-2.80429793, 0.24127801, 0.01363705, 0.11165777, -0.06487585)
    no.high=c(-6.90681925, 0.69720305, 0.04566552, 1.03622425, 0.38925765)
  }
  if(a==0 & b==0 & c==1){
    # PSA, age, race, familyhistory
    no.low=c(-2.92983751, 0.23714373, 0.01463232, 0.11765430, 0.27095959)
    no.high=c(-6.90439295, 0.69799874, 0.04608130, 1.01787561, 0.22913998)
  }
  if(a==0 & b==0 & c==0){
    # PSA, age, race
    no.low=c(-2.81814489, 0.24044370, 0.01370219, 0.12000825)
    no.high=c(-6.84249970, 0.70043815, 0.04574460, 1.01699029)
  }
  ##### predicting probabilities
  S1=no.low%*%data
  S2=no.high%*%data
  risk.no=round(1/(1+exp(S1)+exp(S2))*100)
  risk.low=round(exp(S1)/(1+exp(S1)+exp(S2))*100)
  risk.high=100-risk.no-risk.low
  ##### Outcome
  risk.outcome=cbind(risk.no,risk.low,risk.high)
  dimnames(risk.outcome)=list(NULL, c('Chance of No Cancer', 'Risk of Low Grade
                                      Cancer', 'Risk of High Grade Cancer'))
  return(risk.outcome)
}
