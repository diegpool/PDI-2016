clear all;close all; clc;

load Rho
for k = 51:53
    
    n = int2str(k);
    f1 = 'Fotos/';
    f2 = '.jpg';
    Foto = strcat(f1,n,f2);
    img = double(imread(Foto))./255;
    d = size(img);
    fprintf(strcat('Foto número',int2str(k),'\n'));
    
    fprintf('Seleccione el anillo interior al lunar \n')
    anLunarL  = roipoly(img);
    fprintf('Seleccione el anillo exterior al lunar \n')
    anPiel1L  = roipoly(img);
    fprintf('Seleccione el anillo de la Piel \n')
    anPiel2L  = roipoly(img);

    anPielL = anPiel2L&(not(anPiel1L));

    close all;

    anLunar = zeros(d(1),d(2),d(3));
    anPiel = anLunar;
    
    anLunar(:,:,1) = anLunarL;
    anLunar(:,:,2) = anLunarL;
    anLunar(:,:,3) = anLunarL;
    anLunar = anLunar.*img;

    anPiel(:,:,1) = anPielL;
    anPiel(:,:,2) = anPielL;
    anPiel(:,:,3) = anPielL;
    anPiel = anPiel.*img;

    nulo = zeros(1,1,3);
    A = zeros(1,1,3);
    B = A;
    numpixA = 0;
    numpixB = 0;

    for i = 1:d(1)
        for j = 1:d(2)
            if(anLunar(i,j,:) ~= nulo);
                A = A + anLunar(i,j,:);
                numpixA = numpixA + 1;
            end

            if(anPiel(i,j,:) ~= nulo);
                B = B + anPiel(i,j,:);
                numpixB = numpixB + 1;
            end
        end
    end

    A = A/numpixA;
    B = B/numpixB;
    
    Rho(:,k) = calRho(A,B)
    save Rho
end



