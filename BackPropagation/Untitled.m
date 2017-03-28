patches = sampleIMAGES;
display_network(patches(:,randi(size(patches,2),200,1)),8);


%  Obtain random parameters theta
theta = initializeParameters(hiddenSize, visibleSize);
