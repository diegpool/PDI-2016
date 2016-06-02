clear all;close all; clc;

img = double(imread('Foto.png'))./255;
d = size(img);
%%
anLunarL  = roipoly(img);
anPiel1L  = roipoly(img);
anPiel2L  = roipoly(img);

anPielL = anPiel2L&(not(anPiel1L));

close all;
%%
anLunar = zeros(480,640,3);
anLunar(:,:,1) = anLunarL;
anLunar(:,:,2) = anLunarL;
anLunar(:,:,3) = anLunarL;
anLunar = anLunar.*img;

anPiel = zeros(480,640,3);
anPiel(:,:,1) = anPielL;
anPiel(:,:,2) = anPielL;
anPiel(:,:,3) = anPielL;
anPiel = anPiel.*img;
%%
nulo = zeros(1,1,3);
for i = 1:d(1)
    for j = 1:d(2)
        if(anLunar(i,j,:) ~= nulo);
            
        end  
    end
end
        
