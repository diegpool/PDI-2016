clear all ; close all; clc;

img = double(imread('Foto.png'))./255;

red(1,1,1)= 70/255; red(1,1,2) = 32/255; red(1,1,3) = 32/255;
%green(1,1,1)= 101/255; green(1,1,2) = 97/255; green(1,1,3) = 97/255; 

d1 = 480;
d2 = 640;

A = zeros(1,1,3);
B = A;
numpixA = 0;
numpixB = 0;
tolRho = 0.15;

for i=1:d1
    for j = 1:d2
        temp = img(i,j,:);
        if( norm3D(temp - red) <= tolRho )
            A = A + temp;
            numpixA = numpixA + 1;
        else
            B = B+temp;
            numpixB = numpixB +1;
        end
    end
end

A = A/numpixA;
B = B/numpixB;
rho = calRho(A,B);

imges=[img(:,1,:) img img(:,end,:)];
imges=[imges(1,:,:); imges ;imges(end,:,:)];
imgBorde=zeros(d1,d2,3);
tolBorde = 1;

for i=1:d1-1;
    for j=1:d2;
    
        Atemp = imges(i+1,j,:);
        Btemp = imges(i+1,j+2,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2=calRho(Btemp,Atemp);
        if (norm(rho-rhotemp)<tolBorde); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<tolBorde;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
        
        Atemp = imges(i,j+1,:);
        Btemp = imges(i+2,j+1,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2=calRho(Btemp,Atemp);
        if (norm(rho-rhotemp)<tolBorde); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<tolBorde;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
    end
    
end


figure;
imshow(img+imgBorde(1:480,1:640,:))

