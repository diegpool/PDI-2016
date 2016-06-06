clear all ; close all; clc;

img = double(imread('Fotos/Foto.png'))./255;
%load Rho2.mat

d = size(img);

%rho = (1/length(Rho))*sum(Rho'); %#ok<UDIM>

imges=[img(:,1,:) img img(:,end,:)];
imges=[imges(1,:,:); imges ;imges(end,:,:)];
imgBorde = zeros(d);
A=[86,53,36];
B=[133,119,63];
rho = calRho(A,B);
tolBorde = 0.7;

for i=1:d(1);
    for j=1:d(2);
    
        Atemp = imges(i+1,j,:);
        Btemp = imges(i+1,j+2,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2= calRho(Btemp,Atemp);

        if (norm(rho-rhotemp)<tolBorde); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<tolBorde;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
        
        Atemp = imges(i,j+1,:);
        Btemp = imges(i+2,j+1,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2= calRho(Btemp,Atemp);

        if (norm(rho-rhotemp)<tolBorde); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<tolBorde;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
        
        Atemp = imges(i,j,:);
        Btemp = imges(i+2,j+2,:);
        rhotemp = calRho(Atemp,Btemp);
        rhotemp2=calRho(Btemp,Atemp);
        if (norm(rho-rhotemp)<tolBorde); 
            imgBorde(i+1,j+1,:)=[1 1 1];
        elseif norm(rho-rhotemp2)<tolBorde;
            imgBorde(i+1,j+1,:)=[1 1 1];
        end
        
        Atemp = imges(i,j+2,:);
        Btemp = imges(i+2,j,:);
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
imshow(img+imgBorde(1:d(1),1:d(2),1:d(3)))

